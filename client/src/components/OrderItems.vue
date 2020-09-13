<template>
  <el-card class="order-items" :body-style="{ padding: '0px' }">
    <h1 class="order-items__title" v-if="title">{{ title }}</h1>
    <el-main class="order-items__body">
      <div v-for="item in order" :key="item.id" class="order-items__cycle">
        <div class="order-items__body-dishes">
          <div class="order-items__body-title">{{ item.name }}</div>
          <div class="order-items__body-action">
            <el-button
              circle
              @click="removeDish(item.id)"
              v-if="item.count === 1"
              class="order-items__body-button"
              icon="el-icon-close"
            />
            <el-button
              circle
              @click="minusDish(item.id)"
              v-if="item.count > 1"
              class="order-items__body-button"
              icon="el-icon-minus"
            />
            {{ item.count }} шт.
            <el-button
              circle
              @click="plusDish(item.id)"
              icon="el-icon-plus"
              class="order-items__body-button"
            />
            <div class="order-items__body-price">
              <i>{{ item.price * item.count }}₽</i>
            </div>
          </div>
        </div>
      </div>
    </el-main>
    <div class="order-items__footer">
      <div>
        Сумма заказа:
        <span class="order-items__footer-price"> {{ totalPrice }}₽ </span>
      </div>
      <span v-if="footerInfo">{{ footerInfo }}</span>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "OrderItems",
  data() {
    return {
      priceClass: ""
    };
  },
  props: {
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
  computed: {
    totalPrice: {
      get() {
        return this.order.reduce(function(result, item) {
          return result + item.count * item.price;
        }, 0);
      }
    }
  },
  methods: {
    removeDish(id) {
      this.$emit("removeDishInOrder", id);
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
  justify-content: center;
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
