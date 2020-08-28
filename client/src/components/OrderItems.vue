<template>
  <el-card class="order-items" :body-style="{ padding: '0px' }">
    <h1 class="order-items__title" v-if="title">{{ title }}</h1>
    <el-main class="order-items__body">
      <div v-for="dish in order" :key="dish[0]" class="order-items__cycle">
        <div class="order-items__body-dishes">
          <div class="order-items__body-title">{{ showDishName(dish[0]) }}</div>
          <div class="order-items__body-action">
            <el-button
              circle
              @click="removeDish(dish[0])"
              v-if="dish[1] === 1"
              class="order-items__body-button"
              icon="el-icon-close"
            />
            <el-button
              circle
              @click="minusDish(dish[0])"
              v-if="dish[1] > 1"
              class="order-items__body-button"
              icon="el-icon-minus"
            />
            {{ dish[1] }} шт.
            <el-button
              circle
              @click="plusDish(dish[0])"
              icon="el-icon-plus"
              class="order-items__body-button"
            />
            <div class="order-items__body-price">
              <i>{{ showDishPrice(dish[0]) * dish[1] }}₽</i>
            </div>
          </div>
        </div>
      </div>
    </el-main>
    <div class="order-items__footer">
      <div>
        Сумма заказа:
        <span class="order-items__footer-price">
          {{ priceCalculation() }}₽</span
        >
      </div>
      <span v-if="footerInfo">{{ footerInfo }}</span>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "OrderItems",
  props: {
    dishes: {
      type: Array,
      default: () => []
    },
    order: {
      type: Array,
      default: () => []
    },
    title: {
      type: String,
      default: ""
    },
    footerInfo: {
      type: String,
      default: ""
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
.order-items {
  margin: 1%;
  border-radius: 10px;
}

.order-items__title {
  font-weight: 100;
  padding: 1%;
  margin: 0;
}

.order-items__body {
  max-height: 300px;
}

.order-items__body-dishes {
  display: flex;
  flex-wrap: wrap;
  margin: 1%;
  align-items: center;
}
.order-items__body-button {
  margin: 0 10px 0 10px;
}
.order-items__body-title {
  text-align: left;
  width: 50%;
  min-width: 250px;
}
.order-items__body-price {
  color: orange;
  text-align: left;
  width: 20%;
}
.order-items__body-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 50%;
  min-width: 250px;
}
.order-items__footer {
  display: flex;
  flex-direction: column;
  font-size: 20px;
  min-height: 70px;
  align-items: flex-end;
  justify-content: space-between;
  margin: 2%;
}
.order-items__footer-price {
  color: orange;
  font-size: 35px;
  border-bottom: 1px solid #999999;
  margin-right: 20px;
}
.order-items__cycle {
  border-bottom: 1px solid #999999;
}
</style>
