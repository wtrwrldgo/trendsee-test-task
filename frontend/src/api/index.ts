import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export interface Publication {
  id: number
  user_id: number
  title: string
  content: string
  created_at: string
  updated_at: string
}

export interface PaginatedPublications {
  items: Publication[]
  total: number
  limit: number
  offset: number
}

export interface User {
  id: number
  name: string
  created_at: string
}

export const createUser = (name: string) =>
  api.post<{ user: User; token: string }>('/users', { name })

export const getUserToken = (userId: number) =>
  api.get<{ token: string }>(`/users/${userId}/token`)

export const getUserPublications = (userId: number, limit = 10, offset = 0) =>
  api.get<PaginatedPublications>(`/publications/user/${userId}`, {
    params: { limit, offset },
  })

export const createPublication = (title: string, content: string) =>
  api.post<Publication>('/publications', { title, content })

export default api
