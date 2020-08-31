import Vue from "vue";
import Vuex from "vuex";
import { getDishes } from "@/api/dishes";
import { getPromo } from "@/api/promo";
import createPersistedState from "vuex-persistedstate";
import { authUser, registerUser } from "@/api/users";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    dishes: [],
    order: [],
    token: {
      token: localStorage.getItem("token") || "",
      user: {
        pk: "",
        username: ""
      }
    },
    statusAuth: false,
    promo: []
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
    },
    AUTH_USER: (state, token) => {
      state.token = token;
      state.statusAuth = true;
    },
    LOGOUT: state => {
      state.token.token = "";
      state.token.user.username = "";
      state.token.user.pk = "";
      state.statusAuth = false;
    },
    REGISTER_USER(state) {
      state.statusAuth = true;
    },
    ERROR(state) {
      state.statusAuth = false;
    },
    SET_PROMO_IMAGES: (state, promo) => {
      state.promo = promo;
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
    },
    async signIn({ commit }, user) {
      commit("AUTH_USER", await authUser(user));
    },
    async logout({ commit }) {
      commit("LOGOUT");
      localStorage.removeItem("token");
    },
    async registerNewUser({ commit }, user) {
      try {
        commit("REGISTER_USER", await registerUser(user));
        commit("AUTH_USER", await authUser(user));
      } catch {
        commit("ERROR");
      }
    },
    async getPromoImages({ commit }) {
      commit("SET_PROMO_IMAGES", await getPromo());
    }
  },
  modules: {},
  plugins: [createPersistedState()]
});
