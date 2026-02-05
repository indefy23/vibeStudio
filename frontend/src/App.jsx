import React, { useState, useEffect, useRef } from 'react';
import { Timeline } from './components/Timeline';
import { Preview } from './components/Preview';
import { PromptBar } from './components/PromptBar';
import { Modal } from './components/Modal';
import { MOCK_EDITION } from './mock/edition';
import { api } from './core/api';

function App() {
  const [edition, setEdition] = useState(MOCK_EDITION);
  const [loading, setLoading] = useState(false);
  const [showJsonModal, setShowJsonModal] = useState(false);
  const [lastPlan, setLastPlan] = useState(null);

  // Time State
  const [currentTime, setCurrentTime] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const lastTimeRef = useRef(Date.now());

  // Playback Loop
  useEffect(() => {
    let animId;
    const loop = () => {
      if (isPlaying) {
        const now = Date.now();
        const delta = (now - lastTimeRef.current) / 1000;
        lastTimeRef.current = now;

        setCurrentTime(prev => {
          const nextTime = prev + delta;
          if (nextTime >= edition.meta.duration) {
            setIsPlaying(false);
            return 0; // Loop or stop
          }
          return nextTime;
        });
        animId = requestAnimationFrame(loop);
      }
    };

    if (isPlaying) {
      lastTimeRef.current = Date.now();
      animId = requestAnimationFrame(loop);
    }

    return () => cancelAnimationFrame(animId);
  }, [isPlaying, edition.meta.duration]);

  const handleSeek = (time) => {
    setCurrentTime(time);
    setIsPlaying(false); // Pause on seek
  };

  const handleTogglePlay = (forceState) => {
    setIsPlaying(prev => forceState !== undefined ? forceState : !prev);
  }

  const handleGenerate = async (prompt) => {
    setLoading(true);
    try {
      const newEdition = await api.generate(prompt);
      setEdition(newEdition);
      setLastPlan({
        goal: prompt,
        generated_at: new Date().toISOString(),
        meta: newEdition.meta
      });
    } catch (e) {
      alert("Erro ao gerar: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (file) {
      setLoading(true);
      try {
        // 1. Upload to Backend
        const assetData = await api.uploadAsset(file);

        // 2. Add to Edition
        const newAssetId = assetData.id;
        const blobUrl = URL.createObjectURL(file);

        // Detect Type
        let type = 'video';
        if (file.type.startsWith('image')) type = 'image';
        else if (file.type.startsWith('audio')) type = 'audio';

        const newAsset = {
          id: newAssetId,
          src: blobUrl,
          backendSrc: assetData.src, // Important for FFmpeg
          type: type
        };

        // Find safe spot (end of last clip)
        const mainTrack = edition.timeline.tracks.find(t => t.id === 'main_video' || t.type === 'video');

        let targetTrack = mainTrack;
        // Se não houver track de vídeo, cria uma?
        // Por simplificação assumimos que existe do mock ou cria na primeira
        if (!targetTrack && edition.timeline.tracks.length > 0) targetTrack = edition.timeline.tracks[0];

        const lastClip = targetTrack?.clips ? targetTrack.clips[targetTrack.clips.length - 1] : null;
        const start = lastClip ? lastClip.end : 0.0;

        const newClip = {
          asset: newAssetId,
          start: start,
          end: start + 5.0,
          in: 0.0,
          out: 5.0,
          properties: { scale: 1.0, opacity: 1.0 },
          keyframes: {}
        };

        setEdition(prev => {
          // Deep copy to modify
          const next = JSON.parse(JSON.stringify(prev));
          if (!next.assets[type]) next.assets[type] = [];
          next.assets[type].push(newAsset);

          // Update duration
          next.meta.duration = Math.max(next.meta.duration, start + 5.0);

          // Add clip to track
          const track = next.timeline.tracks.find(t => t.id === targetTrack.id);
          if (track) {
            if (!track.clips) track.clips = [];
            track.clips.push(newClip);
          }

          return next;
        });

      } catch (e) {
        alert("Upload failed: " + e.message);
      } finally {
        setLoading(false);
      }
    }
  };

  const handleRender = async () => {
    setLoading(true);
    try {
      // Prepare Edition for Backend
      const backendEdition = {
        ...edition,
        assets: {
          ...edition.assets,
          video: edition.assets.video.map(a => ({
            ...a,
            src: a.backendSrc || a.src
          }))
        }
      };

      const blob = await api.render(backendEdition);

      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `render_${new Date().getTime()}.mp4`;
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (e) {
      alert("Render failed: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = (trackId, clipIndex) => {
    setEdition(prev => {
      const newTracks = prev.timeline.tracks.map(t => {
        if (t.id !== trackId) return t;

        const newItems = [...(t.clips || t.elements)];
        newItems.splice(clipIndex, 1);

        return t.clips ? { ...t, clips: newItems } : { ...t, elements: newItems };
      });

      return { ...prev, timeline: { ...prev.timeline, tracks: newTracks } };
    });
  };

  /* 
   * Unified Item Handling Helper 
   * Finds track and item regardless of type (clip vs element)
   */
  const findTrackAndItem = (tracks, trackId, itemIndex) => {
    const track = tracks.find(t => t.id === trackId);
    if (!track) return null;

    // Normalize access logic to match Timeline.jsx rendering order
    // In Timeline.jsx we will change to [...clips, ...elements]
    // So index assumes that order.

    const clips = track.clips || [];
    const elements = track.elements || [];

    let item = null;
    let listType = 'clips';

    if (itemIndex < clips.length) {
      item = clips[itemIndex];
      listType = 'clips';
    } else {
      item = elements[itemIndex - clips.length];
      listType = 'elements';
    }

    return { track, item, listType, realIndex: listType === 'clips' ? itemIndex : itemIndex - clips.length };
  };

  const handleMoveClip = (fromTrackId, clipIndex, toTrackId, newStart) => {
    setEdition(prev => {
      const next = JSON.parse(JSON.stringify(prev));

      // 1. Find Source
      const source = findTrackAndItem(next.timeline.tracks, fromTrackId, clipIndex);
      if (!source || !source.item) {
        console.warn("Source item not found", fromTrackId, clipIndex);
        return prev;
      }

      const { track: fromTrack, item, listType, realIndex } = source;

      // Remove from source
      if (listType === 'clips') fromTrack.clips.splice(realIndex, 1);
      else fromTrack.elements.splice(realIndex, 1);

      // 2. Determine Target Track
      let targetTrack = null;

      if (toTrackId === 'NEW_LAYER') {
        // Create generic layer
        targetTrack = {
          id: `Layer ${next.timeline.tracks.length + 1}`,
          type: 'video', // Generic type, we mix anyway
          clips: [],
          elements: []
        };
        next.timeline.tracks.push(targetTrack);
      } else {
        targetTrack = next.timeline.tracks.find(t => t.id === toTrackId);
      }

      if (!targetTrack) return prev;

      // 3. Update Item Time
      const duration = item.end - item.start;
      item.start = Number(newStart.toFixed(2));
      item.end = Number((newStart + duration).toFixed(2));

      // 4. Insert into Target
      const isTextOrShape = item.type === 'text' || item.type === 'shape' || !!item.content;

      if (isTextOrShape) {
        if (!targetTrack.elements) targetTrack.elements = [];
        targetTrack.elements.push(item);
      } else {
        if (!targetTrack.clips) targetTrack.clips = [];
        targetTrack.clips.push(item);
      }

      return next;
    });
  };

  const handleAddText = (content) => {
    setEdition(prev => {
      const next = JSON.parse(JSON.stringify(prev));

      // Find ANY track or create new
      let track = next.timeline.tracks.find(t => t.type === 'overlay' || t.elements);
      if (!track) {
        track = {
          id: "Layer Text",
          type: "overlay",
          clips: [],
          elements: []
        };
        next.timeline.tracks.push(track);
      }

      const start = 0;
      const end = 5.0;

      const newElement = {
        id: `text_${Date.now()}`,
        type: 'text',
        content: content,
        start: start,
        end: end,
        properties: { scale: 1.0, opacity: 1.0, position: { x: 0.5, y: 0.5 }, anchor: 'center' },
        keyframes: {}
      };

      if (!track.elements) track.elements = [];
      track.elements.push(newElement);

      return next;
    });
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1 className="logo">
          <span style={{ color: 'var(--color-primary)' }}>vibe</span>
          <span style={{ color: 'black' }}>Studio</span>
        </h1>
        <div className="badge-container">
          <span className="badge ai">AI-Assisted</span>
          <span className="badge version">Beta v0.9 (Refining)</span>
        </div>
      </header>

      <main className="main-content">
        <div className="sidebar">
          <div className="neo-box" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h3 style={{ fontWeight: 'bold', width: '100%', borderBottom: '2px solid black', marginBottom: '1rem' }}>Monitor</h3>
            <Preview
              edition={edition}
              currentTime={currentTime}
              isPlaying={isPlaying}
              onTogglePlay={handleTogglePlay}
              onRender={handleRender}
            />
          </div>

          <div className="neo-box" style={{ width: '100%' }}>
            <h4 style={{ fontWeight: 'bold', borderBottom: '2px solid black', marginBottom: '0.5rem' }}>Assets</h4>
            <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
              <label className="btn secondary" style={{ width: '100%' }}>
                + Upload Media
                <input type="file" hidden onChange={handleUpload} accept="video/*,image/*,audio/*" />
              </label>

              <button className="btn secondary" style={{ width: '100%', marginTop: '4px' }} onClick={() => {
                // Quick Add Text Logic
                const text = prompt("Enter text content:", "Hello World");
                if (text) handleAddText(text);
              }}>
                + Add Text
              </button>

              <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap', marginTop: '0.5rem' }}>
                {/* Show Videos */}
                {(edition.assets.video || []).map(a => (
                  <div key={a.id} className="neo-box" style={{ padding: '4px', fontSize: '10px', background: '#e0f2fe' }}>V: {a.id}</div>
                ))}
                {/* Show Images */}
                {(edition.assets.image || []).map(a => (
                  <div key={a.id} className="neo-box" style={{ padding: '4px', fontSize: '10px', background: '#fce7f3' }}>I: {a.id}</div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="content-column">
          <PromptBar onGenerate={handleGenerate} isLoading={loading} />

          <div className="neo-box" style={{ background: '#dbeafe', borderLeft: '8px solid #2563eb' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h2 style={{ fontWeight: 'bold', margin: '0 0 0.5rem 0' }}>Current Project</h2>
              {lastPlan && <button className="badge ai cursor-pointer" onClick={() => setShowJsonModal(true)}>View Plan</button>}
            </div>
            <p style={{ margin: 0, opacity: 0.7, fontSize: '0.9rem' }}>
              {lastPlan ? `Goal: ${lastPlan.goal}` : "Conceito de validação para fluxo de edição automatizada."}
            </p>
          </div>

          <Timeline
            edition={edition}
            setEdition={setEdition}
            currentTime={currentTime}
            onSeek={handleSeek}
            onDelete={handleDelete}
            onMoveClip={handleMoveClip}
          />

          <div className="neo-box" style={{ background: '#fefce8', overflow: 'hidden' }}>
            <h4 style={{ fontWeight: 'bold', borderBottom: '2px solid black', paddingBottom: '0.5rem', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ width: '12px', height: '12px', background: 'red', borderRadius: '50%', border: '1px solid black' }}></span>
              DEBUG: Edition JSON Source
            </h4>
            <button className="btn" style={{ fontSize: '10px', padding: '2px 6px', marginBottom: '4px' }} onClick={() => setShowJsonModal(true)}>Full JSON</button>
          </div>
        </div>
      </main>

      <Modal isOpen={showJsonModal} onClose={() => setShowJsonModal(false)} title="Audit: Edition JSON">
        <pre style={{ fontSize: '10px', fontFamily: 'monospace', margin: 0, whiteSpace: 'pre-wrap' }}>
          {JSON.stringify(edition, null, 2)}
        </pre>
      </Modal>
    </div>
  );
}

export default App;
