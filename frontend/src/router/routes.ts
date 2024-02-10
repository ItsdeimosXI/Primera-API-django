import { createRouter, createWebHistory } from 'vue-router'
import HomeVue from '../components/Home/Home.vue'
import GetExpVue from '../components/Expedientes/GetExp.vue'


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomeVue
        },
        {
            path: '/expedientes',
            name: 'Exp',
            component: GetExpVue
        }
]}

)

export default router