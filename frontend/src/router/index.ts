import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserListVue from '@/components/UserList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'user-list',
      component: UserListVue
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    }
  ]
})

export default router
