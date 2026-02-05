const API_URL = "http://localhost:8000";

export const api = {
    async healthCheck() {
        try {
            const res = await fetch(`${API_URL}/health`);
            return await res.json();
        } catch (e) {
            console.error("API Error", e);
            return null;
        }
    },

    async generate(prompt) {
        const res = await fetch(`${API_URL}/api/brain/generate?prompt=${encodeURIComponent(prompt)}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!res.ok) throw new Error("Failed to generate edition");
        return await res.json();
    },

    async uploadAsset(file) {
        const formData = new FormData();
        formData.append('file', file);

        const res = await fetch(`${API_URL}/api/assets/upload`, {
            method: 'POST',
            body: formData
        });
        if (!res.ok) throw new Error("Failed to upload asset");
        return await res.json(); // { id, src, type }
    },

    async render(edition) {
        const res = await fetch(`${API_URL}/api/render`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(edition)
        });
        if (!res.ok) throw new Error("Failed to render video");
        return await res.blob(); // Return Blob for download
    }
};
