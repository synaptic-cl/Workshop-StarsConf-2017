import Vue from 'vue';
import Vuex from 'vuex';
import { getHourTime, getZeroPad } from './utils';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    talksViernes: [],
    talksSabado: [],
    upss: [],
    timeNow: ''
  },
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
        state.timeNow = timeNow.getHours() + ':' + getZeroPad(timeNow.getMinutes());
      }, 1000);
    }
  },
  actions: {
    setTime(context) {
      context.commit('setTime');
    }
  }
});
