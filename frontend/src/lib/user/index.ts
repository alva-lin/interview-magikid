import axios from 'axios'

export interface Pagination<T> {
  current_page: number;
  pages: number;
  total: number;
  data: T[];
}

export type Gender = 'MALE' | 'FEMALE';
export const GenderArray: Gender[] = [ 'MALE', 'FEMALE' ]

export interface User {
  uid: number;
  name: string;
  gender: Gender;
}

const apiClient = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json'
  }
})

export async function addUser(name: string, gender: Gender) {
  const response = await apiClient.post('/user', {
    name,
    gender
  })
  return response.data
}

export async function getUserList(page: number, perPage: number) {
  const response = await apiClient.get<Pagination<User>>(`/user?page=${page}&per_page=${perPage}`)
  return response.data
}

export async function updateUser(id: number, name: string, gender: User['gender']) {
  const response = await apiClient.put(`/user/${id}`, {
    name,
    gender
  })
  return response.data
}
