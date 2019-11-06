import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    lang: 'pt',
  },
  mutations: {
    changeLanguage(state, lang) {
      state.lang = lang;
    },
  },
  getters: {
    lang: state => state.lang,
  },
});
