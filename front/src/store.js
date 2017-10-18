import Vue from "vue";
import Vuex from "vuex";
import { getHourTime, getZeroPad } from "./utils";

Vue.use(Vuex);

/*
  Here we say: Vue, use Vuex (similar to react's redux)
  and Define a store, were we will manage current app State
*/

export const store = new Vuex.Store({
  state: {
    talksViernes: [],
    talksSabado: [],
    upss: [],
    timeNow: ""
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
    },
    getTimeNow: state => {
      return state.timeNow;
    }
  },
  mutations: {
    setTime(state) {
      setInterval(function() {
        const timeNow = new Date();
        state.timeNow =
          timeNow.getHours() + ":" + getZeroPad(timeNow.getMinutes());
      }, 1000);
    }
  },
  actions: {
    setTime(context) {
      context.commit("setTime");
    }
  }
});
