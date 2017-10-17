import Vue from 'vue';
import VueRouter from 'vue-router';
import Timeline from './components/Timeline.vue';
import Nosotros from './components/Nosotros.vue';
Vue.use(VueRouter);

const routes = [
  {
    path: '/agenda/:dia',
    component: Timeline
  },
  {
    path: '/nosotros',
    component: Nosotros
  }
];

export const router = new VueRouter({ routes });
