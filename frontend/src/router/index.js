import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import DashboardPage from '@/views/DashboardPage.vue';
import AnalyticsPage from '@/views/AnalyticsPage.vue';

const routes = [
    {
        path: '/',
        component: HomePage,
        meta: { title: 'Home - ThermoStats' },
    },
    {
        path: '/dashboard',
        component: DashboardPage,
        meta: { title: 'Dashboard - ThermoStats' },
    },
    {
        path: '/analytics',
        component: AnalyticsPage,
        meta: { title: 'Analytics - ThermoStats' },
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const defaultTitle = 'MyApp';
    document.title = to.meta?.title ?? defaultTitle;
    next();
});

export default router;