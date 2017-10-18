import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

/*
  Here we say: Vue, use Vuex (similar to react's redux)
  and Define a store, were we will manage current app State
*/

export const store = new Vuex.Store({
  state: {
    talksViernes: [],
    talksSabado: [],
    upss: []
  },
  /*
    We define getters (https://vuex.vuejs.org/en/getters.html)
    for state's attribute. 
  */
  getters: {
    talksViernes: state => {
      return state.talksViernes;
    },
    talksSabado: state => {
      return state.talksSabado;
    },
    noData: state => {
      return state.upss;
    }
  }
});
