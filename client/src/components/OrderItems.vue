<template>
  <div class="order">
    <h2 class="order__title" v-if="title">{{ title }}</h2>
    <div class="order__body">
      <transition-group name="fade" mode="out-in">
        <div v-for="item in order" :key="item.id" class="order__body-dishes">
          <div class="order__body-title">{{ item.name }}</div>
          <div class="order__body-action">
            <el-button
              circle
              @click="removeDish(item.id)"
              v-if="item.count === 1"
              class="order__body-button"
              icon="el-icon-close"
            />
            <el-button
              circle
              @click="minusDish(item.id)"
              v-if="item.count > 1"
              class="order__body-button"
              icon="el-icon-minus"
            />
            {{ item.count }} шт.
            <el-button
              circle
              @click="plusDish(item.id)"
              icon="el-icon-plus"
              class="order__body-button"
            />
            <div class="order__body-price">
              <i>{{ item.price * item.count }}₽</i>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    <div class="order__footer">
      Сумма заказа:
      <animated-number :number="totalPrice" class="order__footer-price" />
    </div>
    <slot name="footerInfo" />
  </div>
</template>

<script>
import AnimatedNumber from "@/components/AnimatedNumber";

export default {
  name: "OrderItems",
  components: { AnimatedNumber },
  props: {
    order: {
      type: Array,
      default: () => []
    },
    title: {
      type: String,
      default: ""
    }
  },
  computed: {
    totalPrice() {
      return this.$store.getters.totalPrice;
    },
    dishes() {
      return this.$store.getters.dishes;
    }
  },
  methods: {
    removeDish(id) {
      this.$store.dispatch("removeDish", id);
    },
    plusDish(id) {
      this.$store.dispatch("increment", id);
    },
    minusDish(id) {
      this.$store.dispatch("decrement", id);
    }
  }
};
</script>

<style scoped>
.order {
  margin: 1%;
  border-radius: 10px;
  background-color: white;
}

.order__title {
  font-weight: 100;
  padding: 1%;
  margin: 0;
}

.order__body {
  max-height: 250px;
  min-height: 50px;
  overflow: auto;
  width: 100%;
  border-bottom: 2px solid #999999;
}

.order__body-dishes {
  display: flex;
  flex-wrap: wrap;
  margin: 1%;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #999999;
}

.order__body-button {
  margin: 0 10px 0 10px;
}

.order__body-title {
  text-align: left;
  width: 50%;
  min-width: 250px;
}

.order__body-price {
  color: orange;
  text-align: left;
  width: 20%;
}

.order__body-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 50%;
  min-width: 250px;
}

.order__footer {
  display: flex;
  font-size: 20px;
  min-height: 70px;
  align-items: center;
  width: 100%;
  justify-content: flex-end;
}

.order__footer-price {
  color: orange;
  font-size: 35px;
  border-bottom: 1px solid #999999;
  margin-right: 20px;
  margin-bottom: 5px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

@media screen and (max-width: 700px) {
  .order__footer {
    font-size: 12px;
  }

  .order__title {
    font-size: 20px;
  }

  .order__body-title {
    font-size: 15px;
  }

  .order__body-action {
    font-size: 15px;
  }
}
</style>
