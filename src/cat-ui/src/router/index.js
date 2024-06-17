import { createRouter, createWebHistory } from 'vue-router'

import Home from '../components/Home.vue'
import InputPage from '../components/InputPage.vue'
import ResultPage from '../components/ResultPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/input',
    name: 'input',
    component: InputPage
  },
  {
    path: '/result',
    name: 'result',
    component: ResultPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
