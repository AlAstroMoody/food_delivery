import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Order from "@/views/Order.vue";
import Delivery from "@/views/Delivery.vue";
import Profile from "@/views/Profile";
import About from "@/views/About";
import Map from "@/views/Map";
import NotFoundComponent from "@/views/NotFoundComponent";
import store from "@/store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    beforeEnter(from, to, next) {
      store.dispatch("setDishes");
      store.dispatch("setCategories");
      next();
    }
  },
  {
    path: "/order/",
    name: "Order",
    component: Order
  },
  {
    path: "/delivery/",
    name: "Delivery",
    component: Delivery
  },
  {
    path: "/map/",
    name: "Map",
    component: Map
  },
  {
    path: "/profile/",
    name: "Profile",
    component: Profile
  },
  {
    path: "/about/",
    name: "About",
    component: About
  },
  { path: "*", component: NotFoundComponent }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
