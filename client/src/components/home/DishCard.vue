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
  height: auto;
}

.el-card__body {
  width: 100%;
}

.dish__image {
  margin: auto;
  width: 276px;
  height: 276px;
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

@media screen and (max-width: 960px) {
  .dish__image {
    margin: auto;
    width: 190px;
    height: 190px;
  }
  .dish__title {
    font-size: 16px;
  }
  .dish__button {
    padding: 10px;
    font-size: 15px;
  }
  .dish__order {
    font-size: 17px;
  }
}
@media screen and (max-width: 600px) {
  .dish__image {
    margin: auto;
    width: 148px;
    height: 148px;
  }
  .dish__order {
    font-size: 12px;
  }
  .dish__button {
    font-size: 12px;
  }
  .dish__order {
    font-size: 14px;
  }
  .dish__title {
    font-size: 10px;
    min-height: 60px;
  }
}
</style>
