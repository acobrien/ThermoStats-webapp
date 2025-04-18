import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import DashboardPage from "@/views/DashboardPage.vue";
import AnalyticsPage from "@/views/AnalyticsPage.vue";

const routes = [
    { path: '/', component: HomePage },
    { path: '/dashboard', component: DashboardPage },
    { path: '/analytics', component: AnalyticsPage }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router