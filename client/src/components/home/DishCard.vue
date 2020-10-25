<template>
  <el-card class="dish" :body-style="{ padding: '0px' }" shadow="hover">
    <div class="dish__image-box">
      <el-image :src="dish.image" class="dish__image" @click="showModal" />
    </div>
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
  height: auto;
}

.dish__image-box {
  display: flex;
  width: 100%;
  height: 298px;
}

.el-card__body {
  width: 100%;
}

.dish__image {
  margin: auto;
  width: 100%;
  height: 100%;
}

.dish__title {
  font-size: 21px;
  font-weight: lighter;
  padding: 5px;
  min-height: 120px;
  margin: 6px;
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

@media screen and (max-width: 700px) {
  .dish__title {
    font-size: 16px;
  }
  .dish__button {
    padding: 10px;
    font-size: 15px;
  }
  .dish__image-box {
    width: 100%;
    min-height: 148px;
    height: auto;
  }
}
</style>
