import Vue from "vue";
import Vuex from "vuex";
import { getDishes } from "../api/dishes";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    dishes: [],
    order: []
  },
  mutations: {
    SET_DISHES: (state, dishes) => {
      state.dishes = dishes;
    },
    ORDER: (state, order) => {
      state.order = order;
    },
    EDIT_ORDER: (state, payload) => {
      const index = state.order.findIndex(original => original[0] === payload);
      const dish = state.order.find(original => original[0] === payload);
      if (index === -1) {
        state.order.push([payload, 1]);
      } else {
        const count = dish.pop();
        state.order.splice(index, 1, [payload, count + 1]);
      }
    },
    REMOVE_DISH_IN_ORDER: (state, payload) => {
      const index = state.order.findIndex(original => original[0] === payload);
      state.order.splice(index, 1);
    },
    DECREASE_QUANTITY_DISH_IN_ORDER: (state, payload) => {
      const index = state.order.findIndex(original => original[0] === payload);
      const dish = state.order.find(original => original[0] === payload);
      const count = dish.pop();
      if (count > 1) {
        state.order.splice(index, 1, [payload, count - 1]);
      } else state.order.splice(index, 1);
    }
  },
  actions: {
    async getAllDishes({ commit }) {
      commit("SET_DISHES", await getDishes());
    },
    async editOrder({ commit }, payload) {
      commit("EDIT_ORDER", payload);
    },
    async removeDishInOrder({ commit }, payload) {
      commit("REMOVE_DISH_IN_ORDER", payload);
    },
    async decreaseQuantityInOrder({ commit }, payload) {
      commit("DECREASE_QUANTITY_DISH_IN_ORDER", payload);
    }
  },
  modules: {}
});
