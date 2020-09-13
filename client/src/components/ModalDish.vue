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
            <img src="../assets/item_weight.png" />
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
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  background: rgba(62, 62, 62, 0.4);
  z-index: 999;
  min-width: 350px;
  bottom: -1840%;
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
  width: 60%;
  min-width: 380px;
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
</style>
