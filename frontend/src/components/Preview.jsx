import React, { useRef, useEffect, useState } from 'react';

export function Preview({ edition, currentTime, isPlaying, onTogglePlay, onRender }) {
    const canvasRef = useRef(null);
    const videoRef = useRef(null);
    const [activeVideoSrc, setActiveVideoSrc] = useState(null);

    // 1. Determine active video clip based on currentTime
    useEffect(() => {
        // Find FIRST track with valid clip at this time
        // We prioritize tracks by order (first in array = top or bottom? usually tracks[0] is background or top)
        // Let's iterate all video tracks.
        const videoTracks = edition.timeline.tracks.filter(t => t.type === 'video');
        let activeClip = null;

        // Simple z-index logic: Later tracks cover earlier tracks? Or first is main?
        // Usually Track 1 is top? Or Track 1 is base?
        // In array: [0, 1, 2]. Map renders 0, then 1, then 2. So 2 is on top.
        // So we should search in reverse order if we want "Topmost" visible.
        // Let's reverse for search.
        const reversedTracks = [...videoTracks].reverse();

        for (const track of reversedTracks) {
            const clip = track.clips.find(c => currentTime >= c.start && currentTime < c.end);
            if (clip) {
                activeClip = clip;
                break; // Found top-most clip
            }
        }

        if (activeClip) {
            // Find asset source
            // Note: edition.assets might be split by type now? 
            // We should check all asset lists or just video?
            // Clip has asset ID.
            let asset = null;
            if (edition.assets.video) asset = edition.assets.video.find(a => a.id === activeClip.asset);
            // If not found, check others? (User might put image in video track?)

            if (asset && asset.src !== activeVideoSrc) {
                setActiveVideoSrc(asset.src);
                // When source changes, seek to correct offset
                if (videoRef.current) {
                    // Calculate offset into the source video
                    // globalTime - clipStart = timeIntoClip
                    // timeIntoClip + clipInPoint = timeIntoAsset
                    videoRef.current.currentTime = (currentTime - activeClip.start) + (activeClip.in || 0);
                }
            } else if (asset && videoRef.current) {
                // Sync time if drifting (simple sync)
                const expectedVideoTime = (currentTime - activeClip.start) + (activeClip.in || 0);
                // Sync only if diff > 0.3s (frame drop)
                if (Math.abs(videoRef.current.currentTime - expectedVideoTime) > 0.3) {
                    videoRef.current.currentTime = expectedVideoTime;
                }
            }
        } else {
            setActiveVideoSrc(null);
        }
    }, [currentTime, edition, activeVideoSrc]);

    // 2. Playback Control
    useEffect(() => {
        if (videoRef.current) {
            if (isPlaying) videoRef.current.play().catch(e => console.log("Play error", e));
            else videoRef.current.pause();
        }
    }, [isPlaying, activeVideoSrc]);

    // 3. Render Loop
    useEffect(() => {
        let animId;
        const render = () => {
            const canvas = canvasRef.current;
            const ctx = canvas?.getContext('2d');
            if (!canvas || !ctx) return;

            // Clear
            ctx.fillStyle = 'black';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw Video Frame
            // Render Loop: Iterate ALL tracks from bottom (0) to top
            edition.timeline.tracks.forEach(track => {
                // Mix both buckets
                const items = [...(track.clips || []), ...(track.elements || [])];

                // Filter active at current time
                const activeItems = items.filter(item =>
                    currentTime >= item.start && currentTime < item.end
                );

                activeItems.forEach(item => {
                    // TYPE: VIDEO / IMAGE
                    if (item.asset) {
                        const vidAsset = edition.assets.video?.find(a => a.id === item.asset);
                        const imgAsset = edition.assets.image?.find(a => a.id === item.asset);

                        if (vidAsset) {
                            // Draw videoRef if source matches active
                            if (videoRef.current && activeVideoSrc === vidAsset.src) {
                                ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
                            }
                        } else if (imgAsset) {
                            // Draw Image
                            // Quick load - in real app use caching
                            const img = new Image();
                            img.src = imgAsset.src;
                            if (img.complete) {
                                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                            }
                        }
                    }

                    // TYPE: TEXT / OVERLAY
                    else if (item.type === 'text' || item.content) {
                        ctx.save();
                        const x = (item.properties.position?.x ?? 0.5) * canvas.width;
                        const y = (item.properties.position?.y ?? 0.5) * canvas.height;
                        const scale = item.properties.scale ?? 1.0;

                        ctx.translate(x, y);
                        ctx.scale(scale, scale);
                        ctx.fillStyle = 'white';
                        ctx.textAlign = item.properties.anchor === 'center' ? 'center' : 'left';
                        ctx.font = 'bold 30px Arial';
                        ctx.shadowColor = 'black';
                        ctx.shadowBlur = 4;
                        ctx.lineWidth = 2;
                        ctx.strokeText(item.content, 0, 0);
                        ctx.fillText(item.content, 0, 0);
                        ctx.restore();
                    }
                });
            });

            animId = requestAnimationFrame(render);
        };

        animId = requestAnimationFrame(render);
        return () => cancelAnimationFrame(animId);
    }, [edition, currentTime, activeVideoSrc]);

    return (
        <div className="" style={{ width: '100%' }}>
            <div className="monitor">
                <canvas ref={canvasRef} width={360} height={640} style={{ width: '100%', height: '100%' }} />
                <video
                    ref={videoRef}
                    src={activeVideoSrc}
                    style={{ display: 'none' }}
                    muted
                    playsInline
                    loop={false}
                />
            </div>

            <div className="controls">
                <button className="btn" style={{ width: '48px' }} onClick={onTogglePlay}>
                    {isPlaying ? '⏸' : '▶'}
                </button>
                <button className="btn dark" style={{ width: '48px' }} onClick={() => onTogglePlay(false)}>
                    ■
                </button>
                <button className="btn accent" style={{ flex: 1, fontWeight: 'bold' }} onClick={onRender}>RENDER</button>
            </div>
            <div style={{ textAlign: 'center', fontFamily: 'monospace', fontSize: '12px', marginTop: '4px' }}>
                {currentTime.toFixed(2)}s / {edition.meta.duration.toFixed(2)}s
            </div>
        </div>
    );
}
