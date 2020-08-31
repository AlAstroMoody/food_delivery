<template>
  <el-card class="slick-bag" :body-style="{ padding: '0px' }">
    <div class="slick-bag__header">Ваш заказ</div>
    <div class="slick-bag__body" v-if="order.length === 0">
      Нажмите «ЗАКАЗАТЬ» чтобы товар добавился к заказу.
    </div>
    <OrderItems
      :order="order"
      :dishes="dishes"
      @addToOrder="addToOrder"
      @decreaseQuantityInOrder="decreaseQuantityInOrder"
      @removeDishInOrder="removeDishInOrder"
      class="slick-bag__order-items"
    />
    <div class="slick-bag__footer">
      <el-button
        round
        class="slick-bag__button"
        @click="placeInOrder"
        :disabled="!isButtonDisabled()"
      >
        Оформить заказ
      </el-button>
    </div>
  </el-card>
</template>

<script>
import OrderItems from "@/components/OrderItems";
export default {
  name: "SlickBag",
  components: { OrderItems },
  props: {
    dishes: {
      type: Array,
      default: () => []
    },
    order: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    placeInOrder() {
      this.$router.push({ name: "Order" });
    },
    isButtonDisabled() {
      return this.order.length > 0;
    },
    addToOrder(id) {
      this.$emit("addToOrder", id);
    },
    removeDishInOrder(id) {
      this.$emit("removeDishInOrder", id);
    },
    decreaseQuantityInOrder(id) {
      this.$emit("decreaseQuantityInOrder", id);
    }
  }
};
</script>

<style scoped>
.slick-bag {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
}
.slick-bag__header {
  padding: 4%;
  background: #e5e5e5;
  font-size: 35px;
  font-weight: 100;
}
.slick-bag__body {
  padding: 8%;
  font-size: 19px;
  border-bottom: 1px solid #e5e5e5;
}
.slick-bag__footer {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #e5e5e5;
  font-size: 55px;
  padding: 15px 0;
}

.slick-bag__button {
  font-size: 30px;
  background: #f2f2f2;
}

.slick-bag__order-items {
  font-size: 20px;
}
</style>
