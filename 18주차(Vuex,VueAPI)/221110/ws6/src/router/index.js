import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPage from '@/views/AllTodoPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'alltodopage',
    component: AllTodoPage
  },
  {
    path: '/important',
    name: 'important',
    component: () => import('@/views/ImportantTodoPage.vue')
  },
  {
    path: '/today',
    name: 'today',
    component: () => import('@/views/TodayTodoPage.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
