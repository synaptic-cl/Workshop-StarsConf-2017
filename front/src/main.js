import Vue from "vue";
import App from "./App.vue";
import apolloProvider from "./apollo.js";
import { router } from "./router.js";
import { store } from "./store.js";

new Vue({
  el: "#app",
  store,
  router,
  apolloProvider,
  render: h => h(App)
});
