import api from './api'

export async function callBackend(endpoint, data) {
    try {
        const response = await api.post(endpoint, data)
        return response.data
    } catch (error) {
        console.error("API Error:", error)
        throw error
    }
}