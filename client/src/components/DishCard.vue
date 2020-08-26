<template>
  <el-card class="dish" :body-style="{ padding: '0px' }" shadow="hover">
    <el-image :src="dish.image" class="dish__image" @click="showModal" />
    <div class="dish__footer">
      <h1 class="dish__footer-title">{{ dish.name }}</h1>
      <div class="dish__footer-order">
        {{ dish.price }}₽
        <el-button
          round
          class="dish__footer-button"
          @click="addToOrder(dish.id)"
          >Заказать</el-button
        >
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
      this.$notify({
        title: this.dish.name,
        message: "Добавлено в заказ",
        type: "success"
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
  min-width: 200px;
  width: 95%;
  min-height: 300px;
  border-radius: 6%;
  text-align: center;
}
.dish__image {
}
.dish__footer {
  min-height: 150px;
  display: flex;
  flex-direction: column;
  position: relative;
}
.dish__footer-title {
  font-size: 23px;
  line-height: 1;
  max-height: 69px;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 16px 0;
  padding: 0 10px;
  font-weight: lighter;
}
.dish__footer-order {
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
.dish__footer-button {
  background: orange;
  padding: 5%;
  font: 15px/1 "Roboto", sans-serif;
  font-size: 20px;
  color: white;
  box-shadow: 0 0 5px 0 rgba(252, 146, 33, 0.5);
}
</style>
