import React, { useRef, useState, useEffect } from 'react';

export function Timeline({ edition, setEdition, currentTime, onSeek, onDelete, onMoveClip }) {
    const duration = edition.meta.duration || 10; // Fallback duration if 0
    const trackBodyRef = useRef(null);

    const [dragState, setDragState] = useState(null);
    const [hoverTrackId, setHoverTrackId] = useState(null); // Track mouse is hovering over

    const checkOverlap = (trackId, clipIndex, newStart, newEnd) => {
        const track = edition.timeline.tracks.find(t => t.id === trackId);
        if (!track) return false;

        // Mixed Items
        const items = [...(track.clips || []), ...(track.elements || [])];

        return items.some((item, idx) => {
            if (idx === clipIndex) return false; // Ignore self
            // Check intersection
            return (newStart < item.end && newEnd > item.start);
        });
    };

    const handleGlobalMouseMove = (e) => {
        if (!dragState) return;

        const deltaX = e.clientX - dragState.startX;
        const deltaSeconds = (deltaX / dragState.rectWidth) * duration;

        setEdition(prev => {
            const newTracks = [...prev.timeline.tracks];
            const track = newTracks.find(t => t.id === dragState.trackId);
            if (!track) return prev;

            // Unified access
            const clips = track.clips || [];
            const elements = track.elements || [];

            // NOTE: The 'clipIndex' comes from the map iteration order: [...clips, ...elements]
            // So 0..M-1 are clips, M..N are elements.

            let item = null;
            let listType = 'clips';
            let realIndex = dragState.clipIndex;

            if (dragState.clipIndex < clips.length) {
                item = clips[realIndex];
                listType = 'clips';
            } else {
                realIndex = dragState.clipIndex - clips.length;
                item = elements[realIndex];
                listType = 'elements';
            }

            let newClip = { ...item };

            if (dragState.type === 'move') {
                const desiredStart = Math.max(0, dragState.originalStart + deltaSeconds);
                const dur = dragState.originalEnd - dragState.originalStart;
                const desiredEnd = desiredStart + dur;

                // Invariant: Overlap Check
                if (!checkOverlap(dragState.trackId, dragState.clipIndex, desiredStart, desiredEnd)) {
                    newClip.start = Number(desiredStart.toFixed(2));
                    newClip.end = Number(desiredEnd.toFixed(2));
                }
            }
            else if (dragState.type === 'resize-right') {
                const desiredEnd = Math.max(newClip.start + 0.1, dragState.originalEnd + deltaSeconds);
                if (!checkOverlap(dragState.trackId, dragState.clipIndex, newClip.start, desiredEnd)) {
                    newClip.end = Number(desiredEnd.toFixed(2));
                }
            }

            if (listType === 'clips') track.clips[realIndex] = newClip;
            else track.elements[realIndex] = newClip;

            return { ...prev, timeline: { ...prev.timeline, tracks: newTracks } };
        });
    };

    const handleGlobalMouseUp = (e) => {
        if (!dragState) return;

        // Handle Track Change (Vertical Drop)
        if (hoverTrackId && hoverTrackId !== dragState.trackId && onMoveClip) {
            const deltaX = e.clientX - dragState.startX;
            const deltaSeconds = (deltaX / dragState.rectWidth) * duration;
            const newStart = Math.max(0, dragState.originalStart + deltaSeconds);

            // Commit Move to Helper (App.jsx) which handles Cross-Track Logic
            onMoveClip(dragState.trackId, dragState.clipIndex, hoverTrackId, newStart);
        }

        setDragState(null);
    };

    useEffect(() => {
        if (dragState) {
            window.addEventListener('mousemove', handleGlobalMouseMove);
            window.addEventListener('mouseup', handleGlobalMouseUp);
        } else {
            window.removeEventListener('mousemove', handleGlobalMouseMove);
            window.removeEventListener('mouseup', handleGlobalMouseUp);
        }
        return () => {
            window.removeEventListener('mousemove', handleGlobalMouseMove);
            window.removeEventListener('mouseup', handleGlobalMouseUp);
        };
    }, [dragState, edition, hoverTrackId, onMoveClip]);

    const handleDragStart = (e, type, trackId, clipIndex, clip) => {
        e.stopPropagation();
        const trackBody = e.target.closest('.track-body');
        const rect = trackBody.getBoundingClientRect();

        setDragState({
            type,
            trackId,
            clipIndex,
            originalStart: clip.start,
            originalEnd: clip.end,
            startX: e.clientX,
            rectWidth: rect.width
        });
    };

    const handleRulerClick = (e) => {
        const rect = e.currentTarget.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const percent = Math.min(1, Math.max(0, x / rect.width));
        onSeek(percent * duration);
    };

    return (
        <div className="neo-box" style={{ width: '100%', marginTop: '1rem', userSelect: 'none' }}>
            <div className="timeline-header">
                <span>Timeline</span>
                <span className="badge ai">{duration}s</span>
            </div>

            <div className="timeline-canvas">
                {/* Playhead */}
                <div style={{
                    position: 'absolute',
                    left: `${(currentTime / duration) * 100}%`,
                    top: 0, bottom: 0,
                    width: '2px',
                    background: 'red',
                    zIndex: 50,
                    pointerEvents: 'none'
                }}></div>

                {/* Ruler */}
                <div className="ruler" onClick={handleRulerClick} style={{ cursor: 'pointer' }}>
                    {[0, 25, 50, 75, 100].map(p => (
                        <div key={p} style={{ position: 'absolute', left: `${p}%`, height: '100%', borderLeft: '1px solid #999', paddingLeft: '4px', fontSize: '10px' }}>
                            {Math.round(duration * (p / 100) * 10) / 10}s
                        </div>
                    ))}
                </div>

                {edition.timeline.tracks.map((track) => (
                    <div
                        key={track.id}
                        className="track"
                        onMouseEnter={() => setHoverTrackId(track.id)}
                        style={{ border: (dragState && hoverTrackId === track.id) ? '2px dashed blue' : '1px solid black' }}
                    >
                        <div className="track-head">
                            <span style={{ fontSize: '12px', fontWeight: 'bold' }}>{track.id}</span>
                        </div>
                        <div className="track-body">
                            {[...(track.clips || []), ...(track.elements || [])].map((clip, index) => (
                                <div
                                    key={index}
                                    className={`clip ${track.type === 'overlay' ? 'overlay' : ''}`}
                                    onMouseDown={(e) => handleDragStart(e, 'move', track.id, index, clip)}
                                    style={{
                                        left: `${(clip.start / duration) * 100}%`,
                                        width: `${((clip.end - clip.start) / duration) * 100}%`
                                    }}
                                >
                                    <span className="truncate">{clip.asset || clip.content}</span>

                                    {/* Delete Button */}
                                    <button
                                        className="btn secondary"
                                        style={{
                                            position: 'absolute', top: '2px', right: '12px',
                                            padding: '0 4px', fontSize: '8px', lineHeight: '10px',
                                            opacity: 0.8, zIndex: 10, minWidth: '12px', height: '12px'
                                        }}
                                        onMouseDown={(e) => {
                                            e.stopPropagation();
                                            // Confirm? User requested delete functionality.
                                            // Simple confirmation for safety
                                            if (window.confirm("Delete this clip?")) {
                                                if (onDelete) onDelete(track.id, index);
                                            }
                                        }}
                                    >x</button>

                                    <div
                                        className="resize-handle right"
                                        style={{ width: '10px', background: 'rgba(0,0,0,0.5)', right: 0 }}
                                        onMouseDown={(e) => handleDragStart(e, 'resize-right', track.id, index, clip)}
                                    />
                                </div>
                            ))}
                        </div>
                    </div>
                ))}

                {/* NEW TRACK DROP ZONE */}
                <div
                    className="track"
                    style={{
                        border: (dragState && hoverTrackId === 'NEW_LAYER') ? '2px dashed green' : '1px dashed #ccc',
                        opacity: 0.7,
                        justifyContent: 'center',
                        alignItems: 'center',
                        height: '40px',
                        cursor: 'pointer'
                    }}
                    onMouseEnter={() => setHoverTrackId('NEW_LAYER')}
                >
                    <span style={{ fontSize: '10px', color: '#666' }}>+ Drop here to create New Layer</span>
                </div>
            </div>
        </div>
    );
}
