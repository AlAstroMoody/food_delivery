<template>
  <div class="order">
    <el-page-header
      @back="goBack"
      content="Оформление заказа"
      title="На главную страницу"
    >
    </el-page-header>
    <OrderItems
      :order="order"
      :dishes="dishes"
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
      <AuthOrRegister
        v-if="authorization"
        title="Авторизация"
        buttonTitle="Войти"
        auth
        @signIn="signIn"
      />
      <AuthOrRegister
        v-if="!authorization"
        title="Регистрация"
        buttonTitle="Зарегистрироваться"
        @signIn="registerUser"
      />
    </el-card>
    <ClientInfo
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
    goBack() {
      this.$router.push({ name: "Home" });
    },
    async registerUser(formData) {
      await this.$store.dispatch("registerNewUser", formData);
    },
    async signIn(formData) {
      await this.$store.dispatch("signIn", formData);
    },
    async createOrder(formData) {
      if (this.order.length > 0) {
        await addOrder(formData).then(
          response => (this.order_id = response["id"])
        );
        if (this.order_id) {
          for (let position of this.order) {
            let dishesFormData = new FormData();
            dishesFormData.set("dish", position[0]);
            dishesFormData.set("count", position[1]);
            dishesFormData.set("order", this.order_id);
            await addDishesToOrder(dishesFormData);
          }
          await getOrder(this.order_id).then(
            response => (this.orderInfo = response)
          );
          this.$notify.info({
            title: "Заказ №" + this.orderInfo["id"],
            message:
              "на сумму " + this.orderInfo["total_price"] + " отдан в работу!"
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
    addToOrder(id) {
      this.$store.dispatch("editOrder", id);
    },
    removeDishInOrder(id) {
      this.$store.dispatch("removeDishInOrder", id);
      if (this.order.length === 0) {
        this.$router.push({ name: "Home" });
      }
    },
    decreaseQuantityInOrder(id) {
      this.$store.dispatch("decreaseQuantityInOrder", id);
    }
  },
  computed: {
    dishes() {
      return this.$store.state.dishes;
    },
    order() {
      return this.$store.state.order;
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
  min-width: 300px;
}
.order__is-auth {
  text-align: center;
  width: 30%;
  min-width: 300px;
}
.order__client-info {
  width: 30%;
  min-width: 300px;
}
</style>
