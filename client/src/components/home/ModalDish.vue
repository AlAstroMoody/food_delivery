<template>
  <div class="modal" @click.self="close">
    <el-card class="modal__card" :body-style="{ padding: '0px' }">
      <div class="modal__body">
        <div class="modal__left">
          <el-image :src="dish.image_big" class="modal__image"></el-image>
        </div>
        <div class="modal__right">
          <div class="modal__right-header">
            <h1 class="modal__title">{{ dish.name }}</h1>
            <el-link @click="close" class="modal__close">&#10006;</el-link>
          </div>
          <div class="modal__description">
            {{ dish.description }}
          </div>
          <span class="modal__info" v-if="dish.weight > 0">
            <img src="../../assets/item_weight.png" />
            {{ dish.weight }} гр
          </span>
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
  position: fixed;
  top: 0;
  left: 0;
  background: rgba(72, 72, 72, 0.8);
  height: 100%;
  width: 100%;
  z-index: 1000;
  overflow-y: scroll;
}

.modal__body {
  display: flex;
}

.modal__left {
  display: flex;
  width: 50%;
  background-color: #eee;
}

.modal__image {
  margin: auto;
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
  width: 80%;
  min-width: 500px;
  max-width: 1000px;
  z-index: 10;
  border-radius: 10px;
}

.modal__right-header {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
}

.modal__description {
  height: 70%;
  font-size: 17px;
  color: gray;
  padding: 2%;
}

.modal__price {
  color: orange;
  font-size: 23px;
  margin: 5%;
}

.modal__title {
  width: 80%;
  font-size: 23px;
}

.modal__close {
  width: 10%;
  text-align: right;
  padding-top: 20px;
}

.modal__info {
  margin-left: 5%;
}

@media screen and (max-width: 960px) {
  .modal__title {
    font-size: 15px;
  }

  .modal__price {
    font-size: 15px;
  }

  .modal__description {
    font-size: 12px;
  }

  .modal__info {
    font-size: 12px;
  }
}
@media screen and (max-width: 680px) {
  .modal__body {
    flex-direction: column;
    width: 100%;
  }
  .modal__left {
    width: 100%;
  }
  .modal__right {
    width: 100%;
  }
  .modal__card {
    min-width: 90%;
  }
}
</style>
