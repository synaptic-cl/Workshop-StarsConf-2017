import Vue from "vue";
import App from "./App.vue";
import { router } from "./router.js";
import { store } from "./store.js";

new Vue({
  el: "#app",
  store,
  router,
  render: h => h(App)
});
