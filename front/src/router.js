import Vue from "vue";
import VueRouter from "vue-router";
import Timeline from "./components/Timeline.vue";
import Nosotros from "./components/Nosotros.vue";
Vue.use(VueRouter);

/*
  First (above), we say: Vue, use VueRouter,
  then we define a set of routes and using'em we
  create a router. This is router is used in the app.
*/

const routes = [
  {
    path: "/agenda/:dia",
    component: Timeline
  },
  {
    path: "/nosotros",
    component: Nosotros
  }
];

export const router = new VueRouter({ routes });
