<template>
  <el-card class="slick-bag" :body-style="{ padding: '0px' }">
    <div class="slick-bag__header">Ваш заказ</div>
    <div class="slick-bag__body" v-if="order.length === 0">
      Нажмите «ЗАКАЗАТЬ» чтобы товар добавился к заказу.
    </div>
    <el-main class="slick-bag__order">
      <div v-for="dish in order" :key="dish[0]">
        <div>{{ showDishName(dish[0]) }}</div>
        <div class="slick-bag__order-action">
          <i class="el-icon-circle-close" @click="removeDish(dish[0])"></i>
          <i>{{ dish[1] }} шт.</i>
          <i class="el-icon-remove-outline" @click="minusDish(dish[0])"></i>
          <i class="el-icon-circle-plus-outline" @click="plusDish(dish[0])"></i>
          <i>{{ showDishPrice(dish[0]) * dish[1] }}₽</i>
        </div>
      </div>
    </el-main>
    <span class="slick-bag__price"> {{ priceCalculation() }}₽</span>
    <div class="slick-bag__footer">
      <el-button round class="slick-bag__button">Оформить заказ</el-button>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "SlickBag",
  props: {
    dishes: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    order() {
      return this.$store.state.order;
    }
  },
  methods: {
    removeDish(id) {
      this.$emit("removeDishInOrder", id);
    },
    showDishName(id) {
      for (let dish of this.dishes) {
        if (dish.id === id) {
          return dish.name;
        }
      }
    },
    showDishPrice(id) {
      for (let dish of this.dishes) {
        if (dish.id === id) {
          return dish.price;
        }
      }
    },
    priceCalculation() {
      let totalPrice = 0;
      for (let position of this.order) {
        totalPrice +=
          this.dishes.find(original => original.id === position[0]).price *
          position[1];
      }
      return totalPrice;
    },
    plusDish(id) {
      this.$emit("addToOrder", id);
    },
    minusDish(id) {
      this.$emit("decreaseQuantityInOrder", id);
    }
  }
};
</script>

<style scoped>
.slick-bag {
  width: 100%;
  height: 100%;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
  left: 5%;
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
.slick-bag__price {
  display: block;
  color: orange;
  font-size: 35px;
  margin: 3%;
  padding: 2%;
}
.slick-bag__button {
  font-size: 30px;
  background: #f2f2f2;
}
.slick-bag__order {
  display: flex;
  flex-direction: column;
  font-size: 20px;
  text-align: left;
  max-height: 300px;
}
.slick-bag__order-action {
  display: flex;
  margin: 5%;
  justify-content: space-around;
  border-bottom: 1px solid #e5e5e5;
}
</style>
