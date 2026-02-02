import React, { useRef, useState } from 'react';

export function Timeline({ edition, setEdition }) {
    const duration = edition.meta.duration;
    const trackBodyRef = useRef(null);

    // State to track dragging operation
    // { type: 'move' | 'resize', trackId, clipIndex, ...data }
    const [dragState, setDragState] = useState(null);

    const getTimeFromEvent = (e, rect) => {
        const x = e.clientX - rect.left;
        const percent = Math.max(0, Math.min(1, x / rect.width));
        return percent * duration;
    };

    const handleDragStart = (e, type, trackId, clipIndex, clip) => {
        e.stopPropagation();
        // Find the track element width for calc
        // We can't use ref easily for multiple tracks map, so we use e.target.closest
        const trackBody = e.target.closest('.track-body');
        const rect = trackBody.getBoundingClientRect();

        setDragState({
            type,
            trackId,
            clipIndex,
            rawClip: clip,
            originalStart: clip.start,
            originalEnd: clip.end,
            startX: e.clientX,
            rectWidth: rect.width
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

            const clip = { ...track.clips[dragState.clipIndex] }; // or elements

            if (dragState.type === 'move') {
                const newStart = Math.max(0, dragState.originalStart + deltaSeconds);
                const dur = dragState.originalEnd - dragState.originalStart;
                clip.start = Number(newStart.toFixed(2));
                clip.end = Number((newStart + dur).toFixed(2));
            } else if (dragState.type === 'resize-right') {
                const newEnd = Math.max(clip.start + 0.1, dragState.originalEnd + deltaSeconds);
                clip.end = Number(newEnd.toFixed(2));
            }

            // Apply back
            // Warning: This assumes clips is the array we are editing. If overlay, it is elements.
            // For prototype simplicity, checking type
            if (track.clips) track.clips[dragState.clipIndex] = clip;
            else if (track.elements) track.elements[dragState.clipIndex] = clip; // Overlays

            return {
                ...prev,
                timeline: { ...prev.timeline, tracks: newTracks }
            };
        });
    };

    const handleGlobalMouseUp = () => {
        setDragState(null);
    };

    // Add global listeners when dragging
    React.useEffect(() => {
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
    }, [dragState]);

    return (
        <div className="neo-box" style={{ width: '100%', marginTop: '1rem', userSelect: 'none' }}>
            <div className="timeline-header">
                <span>Timeline</span>
                <span className="badge ai">{duration}s</span>
            </div>

            <div className="timeline-canvas">
                {/* Time ruler */}
                <div className="ruler">
                    {[0, 25, 50, 75, 100].map(p => (
                        <div key={p} style={{ position: 'absolute', left: `${p}%`, height: '100%', borderLeft: '1px solid #999', paddingLeft: '4px', fontSize: '10px' }}>
                            {Math.round(duration * (p / 100) * 10) / 10}s
                        </div>
                    ))}
                </div>

                {edition.timeline.tracks.map((track) => (
                    <div key={track.id} className="track">
                        <div className="track-head">
                            <span style={{ fontSize: '12px', fontWeight: 'bold', overflow: 'hidden', textOverflow: 'ellipsis' }}>{track.id}</span>
                            <span style={{ fontSize: '10px', color: '#666', fontFamily: 'monospace' }}>{track.type}</span>
                        </div>

                        <div className="track-body" ref={trackBodyRef}>
                            {/* Render Clips or Elements depending on track type */}
                            {(track.clips || track.elements || []).map((clip, index) => (
                                <div
                                    key={clip.asset || clip.id || index}
                                    className={`clip ${track.type === 'overlay' ? 'overlay' : ''}`}
                                    onMouseDown={(e) => handleDragStart(e, 'move', track.id, index, clip)}
                                    style={{
                                        left: `${(clip.start / duration) * 100}%`,
                                        width: `${((clip.end - clip.start) / duration) * 100}%`
                                    }}
                                    title={`Start: ${clip.start}s | End: ${clip.end}s`}
                                >
                                    <span className="truncate">{clip.asset || clip.content || clip.type}</span>

                                    {/* Resize Handle Right */}
                                    <div
                                        className="resize-handle right"
                                        onMouseDown={(e) => handleDragStart(e, 'resize-right', track.id, index, clip)}
                                    />
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
