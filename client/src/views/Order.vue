<template>
  <div class="order">
    <order-items
      :order="order"
      @addToOrder="addToOrder"
      @decreaseQuantityInOrder="decreaseQuantityInOrder"
      @removeDishInOrder="removeDishInOrder"
      class="orderItems"
      title="В вашем заказе:"
      footerInfo="Сумма минимального заказа от 490 руб, в отдаленные районы от 1290 руб, подробнее об условиях"
    />
    <el-card class="order__is-auth" v-if="!statusAuth">
      Для продолжения необходимо авторизоваться
      <el-switch
        style="display: block"
        v-model="authorization"
        active-color="#13ce66"
        inactive-color="#0088ff"
        active-text="Авторизация"
        inactive-text="Регистрация"
      >
      </el-switch>
      <transition name="fade" mode="out-in">
        <auth-or-register
          v-if="authorization"
          title="Авторизация"
          buttonTitle="Войти"
          auth
          @signIn="signIn"
        />
        <auth-or-register
          v-if="!authorization"
          title="Регистрация"
          buttonTitle="Зарегистрироваться"
          @signIn="registerUser"
        />
      </transition>
    </el-card>
    <client-info
      class="order__client-info"
      @createOrder="createOrder"
      v-if="statusAuth"
    />
  </div>
</template>

<script>
import { addOrder } from "@/api/orders";
import { getOrder } from "@/api/orders";
import { addDishesToOrder } from "@/api/orders";
import OrderItems from "@/components/OrderItems";
import AuthOrRegister from "@/components/AuthOrRegister";
import ClientInfo from "@/components/ClientInfo";
import { mapActions } from "vuex";

export default {
  name: "Order",
  data() {
    return {
      authorization: true,
      order_id: false
    };
  },
  components: {
    OrderItems,
    AuthOrRegister,
    ClientInfo
  },
  methods: {
    async registerUser(formData) {
      await this.$store.dispatch("registerNewUser", formData);
    },
    async signIn(formData) {
      await this.$store.dispatch("signIn", formData);
    },
    async createOrder(formData) {
      if (this.order.length > 0) {
        await addOrder(formData).then(response => (this.newOrder = response));
        if (this.newOrder["id"]) {
          for (let item of this.order) {
            let dishesFormData = new FormData();
            dishesFormData.set("dish", item.id);
            dishesFormData.set("count", item.count);
            dishesFormData.set("order", this.newOrder["id"]);
            await addDishesToOrder(dishesFormData);
          }
          await getOrder(this.newOrder["id"]).then(
            response => (this.orderInfo = response)
          );
          this.$notify.info({
            title: `${this.newOrder["user_name"]}, заказ № ${this.orderInfo["id"]}`,
            message: `на сумму ${this.orderInfo["total_price"]} отдан в работу!`
          });
          if (this.orderInfo["id"]) {
            this.$store.state.order = [];
            this.goBack();
          } else {
            this.$notify.info({
              message: "Произошла непредвиденная ошибка"
            });
          }
        }
      }
    },
    ...mapActions([
      "editOrder",
      "removeDishInOrder",
      "decreaseQuantityInOrder"
    ]),
    // задублированы функции с Home, исправить
    addToOrder(id) {
      this.$store.dispatch("editOrder", this.getDishById(id));
    },
    removeDishInOrder(id) {
      this.$store.dispatch("removeDishInOrder", this.getDishById(id));
    },
    decreaseQuantityInOrder(id) {
      this.$store.dispatch("decreaseQuantityInOrder", this.getDishById(id));
    },
    getDishById(id) {
      for (let i = 0; i < this.dishes.length; i++) {
        if (this.dishes[i]["id"] === id) {
          return {
            id: id,
            name: this.dishes[i]["name"],
            price: this.dishes[i]["price"]
          };
        }
      }
    }
  },
  computed: {
    order() {
      return this.$store.state.order;
    },
    dishes() {
      return this.$store.state.dishes;
    },
    authOrRegister() {
      return this.authorization;
    },
    statusAuth() {
      return this.$store.state.statusAuth;
    }
  }
};
</script>

<style scoped>
.order {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.orderItems {
  width: 50%;
  font-size: 25px;
  min-width: 350px;
}

.order__is-auth {
  text-align: center;
  width: 30%;
  min-width: 350px;
}

.order__client-info {
  width: 40%;
  min-width: 350px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
