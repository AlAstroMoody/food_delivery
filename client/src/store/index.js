import Vue from "vue";
import Vuex from "vuex";
import { getDishes } from "../api/dishes";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    dishes: []
  },
  mutations: {
    SET_DISHES: (state, dishes) => {
      state.dishes = dishes;
    }
  },
  actions: {
    async getAllDishes({ commit }) {
      commit("SET_DISHES", await getDishes());
    }
  },
  modules: {}
});
