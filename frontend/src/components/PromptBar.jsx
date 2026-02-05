import React, { useState } from 'react';

export function PromptBar({ onGenerate, isLoading }) {
    const [prompt, setPrompt] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (prompt.trim()) {
            onGenerate(prompt);
        }
    };

    return (
        <div className="neo-box" style={{ width: '100%', marginBottom: '1rem', background: '#fdf4ff' }}>
            <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '1rem' }}>
                <input
                    className="neo-input"
                    style={{ flex: 1, margin: 0 }}
                    placeholder="Descreva o vídeo que você quer... (ex: 'Cortes rápidos, foco em zoom')"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    disabled={isLoading}
                />
                <button
                    type="submit"
                    className="btn secondary"
                    disabled={isLoading}
                >
                    {isLoading ? "🧠 Thinking..." : "✨ Generate Magic"}
                </button>
            </form>
        </div>
    );
}
