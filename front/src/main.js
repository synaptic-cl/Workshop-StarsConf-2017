import Vue from "vue";
import App from "./App.vue";
import apolloProvider from "./apollo.js";
import { router } from "./router.js";
import { store } from "./store.js";

/*
  The Vue App is defined here. Store, Router and Apollo are given 
  and now are enabled for the entire app.
*/

new Vue({
  el: "#app",
  store,
  router,
  apolloProvider,
  render: h => h(App)
});
