import Vue from 'vue';
import VueRouter from 'vue-router';
import Timeline from './components/Timeline.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/agenda/:dia',
    component: Timeline
  }
];

export const router = new VueRouter({ routes });
