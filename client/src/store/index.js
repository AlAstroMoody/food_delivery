import Vue from "vue";
import Vuex from "vuex";
import { getDishes, getCategories } from "@/api/dishes";
import { getPromo } from "@/api/promo";
import createPersistedState from "vuex-persistedstate";
import { authUser, registerUser } from "@/api/users";
import { getProfile, editProfile } from "@/api/profile";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    dishes: [],
    categories: [],
    order: [],
    token: {
      token: localStorage.getItem("token") || "",
      user: {
        pk: "",
        username: ""
      }
    },
    statusAuth: false,
    promo: [],
    profile: {
      address: "",
      birthday: "",
      id: "",
      name: "",
      phone: "",
      user: ""
    }
  },
  mutations: {
    SET_DISHES: (state, dishes) => {
      state.dishes = dishes;
    },
    SET_CATEGORIES: (state, categories) => {
      state.categories = categories;
    },
    ORDER: (state, order) => {
      state.order = order;
    },
    EDIT_ORDER: (state, payload) => {
      const index = state.order.findIndex(
        original => original["id"] === payload.id
      );
      if (index === -1) {
        state.order.push({
          id: payload.id,
          count: 1,
          name: payload.name,
          price: payload.price
        });
      } else {
        state.order[index].count++;
      }
    },
    REMOVE_DISH_IN_ORDER: (state, payload) => {
      const index = state.order.findIndex(
        original => original["id"] === payload.id
      );
      state.order.splice(index, 1);
    },
    DECREASE_QUANTITY_DISH_IN_ORDER: (state, payload) => {
      const index = state.order.findIndex(
        original => original["id"] === payload.id
      );
      state.order[index].count--;
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
    },
    PROFILE: (state, profile) => {
      state.profile = profile;
    }
  },
  actions: {
    async getAllDishes({ commit }) {
      commit("SET_DISHES", await getDishes());
    },
    async getAllCategories({ commit }) {
      commit("SET_CATEGORIES", await getCategories());
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
    },
    async getUserProfile({ commit }, id) {
      commit("PROFILE", await getProfile(id));
    },
    async editUserProfile({ commit }, id) {
      commit("PROFILE", await editProfile(id));
    }
  },
  getters: {
    dishes(state) {
      return state.dishes;
    },
    dish: state => id => {
      return state.dishes[id];
    }
  },
  modules: {},
  plugins: [createPersistedState()]
});
