const API_BASE_URL = "http://localhost:8000/api/v1";

async function apiRequest(path, {method = "GET", body, token} = {}) {
    const headers = {
        "Content-Type": "application/json",
    };
    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch (`${API_BASE_URL}${path}`, {
        method,
        headers,
        body: body ? JSON.stringify(body) : undefined,
    });

    let data = null;
    try {
        data = await response.json();
    } catch (e) {
        // Response ohne JSON ist okay
    }

    if (!response.ok) {
        const error = new Error(data?.detail || "API request failed");
        error.status = response.status;
        error.data = data;
        throw error;
    }

    return data;
}


export const api = {
    get: (path, options) => apiRequest(path, { ...options, method: "GET" }),
    post: (path, options) => apiRequest(path, { ...options, method: "POST"}),
    put: (path, options) => apiRequest(path, { ...options, method: "PUT" }),
    del: (path, options) => apiRequest(path, { ...options, method: "DELETE" }),
};