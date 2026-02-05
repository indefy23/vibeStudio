import React from 'react';

export function Modal({ isOpen, onClose, title, children }) {
    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4" style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100 }}>
            <div className="absolute inset-0 bg-black/50" style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)' }} onClick={onClose}></div>
            <div className="neo-box relative bg-white max-w-lg w-full max-h-[90vh] overflow-y-auto" style={{ position: 'relative', width: '100%', maxWidth: '600px', background: 'white', maxHeight: '90vh', overflowY: 'auto' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '2px solid black', paddingBottom: '0.5rem', marginBottom: '1rem' }}>
                    <h3 className="text-xl font-bold uppercase">{title}</h3>
                    <button onClick={onClose} className="btn secondary" style={{ padding: '0.2rem 0.5rem' }}>X</button>
                </div>
                {children}
            </div>
        </div>
    );
}
