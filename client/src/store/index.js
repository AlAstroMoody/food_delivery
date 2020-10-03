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
    setDishes: (state, dishes) => {
      state.dishes = dishes;
    },
    setCategories: (state, categories) => {
      state.categories = categories;
    },
    order: (state, order) => {
      state.order = order;
    },
    addNewDishToOrder: (state, payload) => {
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
    removeDish: (state, id) => {
      const index = state.order.findIndex(original => original["id"] === id);
      state.order.splice(index, 1);
    },
    increment: (state, id) => {
      const index = state.order.findIndex(original => original["id"] === id);
      state.order[index].count++;
    },
    decrement: (state, id) => {
      const index = state.order.findIndex(original => original["id"] === id);
      state.order[index].count--;
    },
    auth: (state, token) => {
      state.token = token;
      state.statusAuth = true;
    },
    logout: state => {
      state.token.token = "";
      state.token.user.username = "";
      state.token.user.pk = "";
      state.statusAuth = false;
    },
    register(state) {
      state.statusAuth = true;
    },
    error(state) {
      state.statusAuth = false;
    },
    setPromoImages: (state, promo) => {
      state.promo = promo;
    },
    profile: (state, profile) => {
      state.profile = profile;
    }
  },
  actions: {
    async setDishes({ commit }) {
      commit("setDishes", await getDishes());
    },
    async setCategories({ commit }) {
      commit("setCategories", await getCategories());
    },
    async addNewDishToOrder({ commit }, payload) {
      commit("addNewDishToOrder", payload);
    },
    async removeDish({ commit }, id) {
      commit("removeDish", id);
    },
    async decrement({ commit }, id) {
      commit("decrement", id);
    },
    async increment({ commit }, id) {
      commit("increment", id);
    },
    async auth({ commit }, user) {
      commit("auth", await authUser(user));
    },
    async logout({ commit }) {
      commit("logout");
      localStorage.removeItem("token");
    },
    async register({ commit }, user) {
      try {
        commit("register", await registerUser(user));
        commit("auth", await authUser(user));
      } catch {
        commit("error");
      }
    },
    async setPromoImages({ commit }) {
      commit("setPromoImages", await getPromo());
    },
    async getUserProfile({ commit }, id) {
      commit("profile", await getProfile(id));
    },
    async editUserProfile({ commit }, id) {
      commit("profile", await editProfile(id));
    }
  },
  getters: {
    dishes(state) {
      return state.dishes;
    }
  },
  modules: {},
  plugins: [createPersistedState()]
});
