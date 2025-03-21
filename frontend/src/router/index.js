import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import DashboardPage from "@/views/DashboardPage.vue";

const routes = [
    { path: '/', component: HomePage },
    { path: '/dashboard', component: DashboardPage }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router