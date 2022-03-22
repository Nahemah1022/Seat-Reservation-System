import { createRouter, createWebHistory } from "vue-router";
import Function_Bar from "../components/Function_Bar.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Function_Bar,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
