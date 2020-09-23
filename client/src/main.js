import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import locale from "element-ui/lib/locale/lang/ru-RU";
import Vuelidate from "vuelidate";
import YmapPlugin from "vue-yandex-maps";

const settings = {
  apiKey: "",
  lang: "ru_RU",
  coordorder: "latlong",
  version: "2.1"
};

Vue.use(YmapPlugin, settings);

Vue.use(ElementUI, { locale });
Vue.use(Vuelidate);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
