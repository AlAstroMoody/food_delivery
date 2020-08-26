<template>
  <div class="modal">
    <el-card
      class="modal__card"
      :body-style="{ padding: '0px' }"
      v-on:click.self="close"
    >
      <div class="modal__body">
        <div class="modal__left">
          <el-image :src="dish.image_big"></el-image>
        </div>
        <div class="modal__right">
          <div class="modal__right-header">
            <h1 class="modal__title">{{ dish.name }}</h1>
            <span @click="close">&#10006;</span>
          </div>
          <div class="modal__description">
            {{ dish.description }}
          </div>
          <div class="modal__price">{{ dish.price }}₽</div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "ModalDish",
  methods: {
    close() {
      this.$emit("showModal");
    }
  },
  props: {
    dish: {
      type: Object,
      default: () => {}
    }
  }
};
</script>

<style scoped>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(62, 62, 62, 0.4);
}

.modal__body {
  display: flex;
}
.modal__left {
  width: 50%;
}
.modal__right {
  display: flex;
  flex-direction: column;
  width: 50%;
  background-color: #eee;
}
.modal__card {
  display: flex;
  top: 10%;
  position: fixed;
  width: 60%;

  min-width: 300px;
  z-index: 10;
  border-radius: 5%;
}
.modal__right-header {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
.modal__description {
  height: 70%;
  font-size: 25px;
  padding: 2%;
}
.modal__price {
  color: orange;
  font-size: 30px;
  text-align: center;
}
.modal__title {
  width: 80%;
}
</style>
