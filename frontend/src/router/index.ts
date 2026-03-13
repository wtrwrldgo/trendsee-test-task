import { createRouter, createWebHistory } from 'vue-router'
import FeedView from '../views/FeedView.vue'
import Page1 from '../views/Page1.vue'
import Page2 from '../views/Page2.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: FeedView },
    { path: '/video-cart', component: Page1 },
    { path: '/analysis', component: Page2 },
  ],
})

export default router
