<template>
  <el-card class="dish" :body-style="{ padding: '0px' }" shadow="hover">
    <el-image :src="dish.image" class="dish__image" @click="showModal" />
    <h1 class="dish__title">{{ dish.name }}</h1>
    <div class="dish__order">
      {{ dish.price }}₽
      <el-button round class="dish__button" @click="addToOrder">
        Заказать
      </el-button>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "DishCard",
  props: {
    dish: {
      type: Object,
      default: () => {}
    }
  },
  methods: {
    addToOrder() {
      this.$notify.success({
        title: this.dish.name,
        message: "Добавлено в заказ"
      });
      this.$emit("addToOrder");
    },
    showModal() {
      this.$emit("showModal", this.dish);
    }
  }
};
</script>

<style scoped>
.dish {
  display: flex;
  width: 100%;
  border-radius: 10px;
  text-align: center;
  justify-content: center;
}

.dish__image {
  margin: auto;
  width: 100%;
}

.dish__title {
  font-size: 21px;
  font-weight: lighter;
  padding: 5px;
  min-height: 120px;
}

.dish__order {
  display: flex;
  justify-content: space-around;
  font-size: 25px;
  align-items: center;
  margin: 3%;
  color: orange;
  width: 100%;
}

.dish__button {
  background: orange;
  padding: 15px;
  font-size: 20px;
  color: white;
  box-shadow: 0 0 5px 0 rgba(252, 146, 33, 0.5);
}

@media screen and (max-width: 850px) {
  .dish__title {
    font-size: 18px;
  }
  .dish__order {
    font-size: 18px;
  }
  .dish__button {
    font-size: 17px;
  }
  .dish__title {
    font-size: 19px;
  }
}

@media screen and (max-width: 700px) {
  .dish__title {
    font-size: 16px;
  }
  .dish__order {
    justify-content: center;
  }
  .dish__button {
    margin-left: 15px;
  }
}
@media screen and (max-width: 450px) {
  .dish__button {
    margin-left: 5px;
  }
}
</style>
