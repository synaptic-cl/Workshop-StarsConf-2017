import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    talksViernes: [],
    talksSabado: [],
    upss: []
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
    }
  }
});
