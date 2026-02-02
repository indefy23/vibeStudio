import React from 'react';

export function Preview() {
    return (
        <div className="" style={{ width: '100%' }}>
            {/* Removed outer box class to avoid nesting issues in sidebar */}
            <div className="monitor">
                <span style={{ color: '#666', fontFamily: 'monospace', zIndex: 10, fontSize: '12px' }}>NO SIGNAL</span>
                <div style={{ position: 'absolute', inset: 0, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gridTemplateRows: 'repeat(3, 1fr)', opacity: 0.2, pointerEvents: 'none' }}>
                    {[...Array(9)].map((_, i) => (
                        <div key={i} style={{ border: '1px solid white' }}></div>
                    ))}
                </div>
            </div>

            <div className="controls">
                <button className="btn" style={{ width: '48px' }}>▶</button>
                <button className="btn dark" style={{ width: '48px' }}>■</button>
                <button className="btn accent" style={{ flex: 1, fontWeight: 'bold' }}>RENDER</button>
            </div>
        </div>
    );
}
