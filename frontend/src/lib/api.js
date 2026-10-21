// Base URL: use the env var when set; fall back to same-origin (works with Vite proxy).
const BASE = (import.meta.env.VITE_API_BASE_URL || '').replace(/\/$/, '')

async function apiFetch(path, options = {}) {
  const url = `${BASE}${path}`
  const response = await fetch(url, options)
  const data = await response.json().catch(() => ({}))
  if (!response.ok) {
    const detail = typeof data.detail === 'string'
      ? data.detail
      : Array.isArray(data.detail)
        ? data.detail.map(e => e.msg || JSON.stringify(e)).join(', ')
        : 'Request failed.'
    throw new Error(detail)
  }
  return data
}

export async function createItinerary(payload) {
  return apiFetch('/api/itinerary', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
}

export async function getHealth() {
  return apiFetch('/api/health')
}
