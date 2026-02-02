import React, { useState } from 'react';
import { Timeline } from './components/Timeline';
import { Preview } from './components/Preview';
import { MOCK_EDITION } from './mock/edition';

function App() {
  const [edition, setEdition] = useState(MOCK_EDITION);

  const handleUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      // Criar um novo asset video e adicionar ao topo
      const newAssetId = `v${Date.now()}`;
      const newAsset = { id: newAssetId, src: URL.createObjectURL(file), type: 'video' };

      const newClip = {
        asset: newAssetId,
        start: 0.0,
        end: 5.0, // Default 5s
        in: 0.0,
        out: 5.0,
        properties: { scale: 1.0, opacity: 1.0 },
        keyframes: {}
      };

      setEdition(prev => ({
        ...prev,
        assets: { ...prev.assets, video: [...prev.assets.video, newAsset] },
        timeline: {
          ...prev.timeline,
          tracks: prev.timeline.tracks.map(t =>
            t.id === 'main_video'
              ? { ...t, clips: [...t.clips, newClip] }
              : t
          )
        }
      }));
    }
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
          <span className="badge version">Alpha v0.2.1</span>
        </div>
      </header>

      <main className="main-content">
        <div className="sidebar">
          <div className="neo-box" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h3 style={{ fontWeight: 'bold', width: '100%', borderBottom: '2px solid black', marginBottom: '1rem' }}>Monitor</h3>
            <Preview />
          </div>

          <div className="neo-box" style={{ width: '100%' }}>
            <h4 style={{ fontWeight: 'bold', borderBottom: '2px solid black', marginBottom: '0.5rem' }}>Assets</h4>
            <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
              <label className="btn secondary" style={{ width: '100%' }}>
                + Upload Video
                <input type="file" hidden onChange={handleUpload} accept="video/*" />
              </label>
              <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap', marginTop: '0.5rem' }}>
                {edition.assets.video.map(a => (
                  <div key={a.id} className="neo-box" style={{ padding: '4px', fontSize: '10px' }}>{a.id}</div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="content-column">
          <div className="neo-box" style={{ background: '#dbeafe', borderLeft: '8px solid #2563eb' }}>
            <h2 style={{ fontWeight: 'bold', margin: '0 0 0.5rem 0' }}>Project: Social Media Teaser</h2>
            <p style={{ margin: 0, opacity: 0.7, fontSize: '0.9rem' }}>Conceito de validação para fluxo de edição automatizada.</p>
          </div>

          <Timeline edition={edition} setEdition={setEdition} />

          <div className="neo-box" style={{ background: '#fefce8', overflow: 'hidden' }}>
            <h4 style={{ fontWeight: 'bold', borderBottom: '2px solid black', paddingBottom: '0.5rem', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ width: '12px', height: '12px', background: 'red', borderRadius: '50%', border: '1px solid black' }}></span>
              DEBUG: Edition JSON Source
            </h4>
            <div style={{ background: 'white', border: '2px solid black', padding: '0.5rem', borderRadius: '4px', boxShadow: 'inset 0 0 5px rgba(0,0,0,0.1)', maxHeight: '200px', overflow: 'auto' }}>
              <pre style={{ fontSize: '10px', fontFamily: 'monospace', margin: 0 }}>
                {JSON.stringify(edition, null, 2)}
              </pre>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
