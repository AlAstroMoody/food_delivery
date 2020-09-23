<template>
  <el-card class="dish" :body-style="{ padding: '0px' }" shadow="hover">
    <div class="dish__header">
      <el-image :src="dish.image" class="dish__image" @click="showModal" />
    </div>
    <div class="dish__footer">
      <h1 class="dish__title">{{ dish.name }}</h1>
      <div class="dish__order">
        {{ dish.price }}₽
        <el-button round class="dish__button" @click="addToOrder(dish.id)">
          Заказать
        </el-button>
      </div>
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
    addToOrder(id) {
      this.$notify.success({
        title: this.dish.name,
        message: "Добавлено в заказ"
      });
      this.$emit("addToOrder", id);
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
  border-radius: 6%;
  text-align: center;
  justify-content: center;
}
.dish__header {
  min-height: 300px;
  display: flex;
  justify-content: center;
}

.dish__image {
  margin: auto;
  width: 100%;
}

.dish__footer {
  min-height: 200px;
  display: flex;
  flex-direction: column;
  position: relative;
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
  margin: 2%;
  color: orange;
  position: absolute;
  width: 100%;
  bottom: 2%;
}

.dish__button {
  background: orange;
  padding: 5%;
  font-size: 20px;
  color: white;
  box-shadow: 0 0 5px 0 rgba(252, 146, 33, 0.5);
}

@media screen and (max-width: 1400px) {
  .dish__header {
    min-height: 50%;
    max-height: 60%;

    min-width: 250px;
  }
}
@media screen and (max-width: 850px) {
  .dish__footer-title {
    font-size: 18px;
  }
  .dish__footer-order {
    font-size: 18px;
  }
  .dish__footer-button {
    font-size: 17px;
  }
}

@media screen and (max-width: 700px) {
  .dish__footer-title {
    font-size: 16px;
  }
  .dish__footer {
    min-height: 100px;
  }
}
</style>
