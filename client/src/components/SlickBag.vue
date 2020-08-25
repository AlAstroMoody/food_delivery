<template>
  <el-card class="slick-bag" :body-style="{ padding: '0px' }">
    <div class="slick-bag__header">Ваш заказ</div>
    <div class="slick-bag__body">
      Нажмите «ЗАКАЗАТЬ» чтобы товар добавился к заказу.
    </div>
    <span class="slick-bag__price"> {{ totalPrice }}₽</span>
    <div class="slick-bag__footer">
      <el-button round class="slick-bag__button">Оформить заказ</el-button>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "SlickBag",
  data() {
    return {
      // потом перенести в computed
      totalPrice: 0
    };
  }
};
</script>

<style scoped>
.slick-bag {
  width: 100%;
  height: 100%;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
}
.slick-bag__header {
  padding: 15px 0;
  background: #e5e5e5;
  font-size: 35px;
  font-weight: 100;
}
.slick-bag__body {
  width: 90%;
  height: 100%;
  padding: 8%;
  font-size: 19px;
  border-bottom: 1px solid #e5e5e5;
}
.slick-bag__footer {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #e5e5e5;
  font-size: 55px;
  padding: 15px 0;
}
.slick-bag__price {
  display: block;
  color: orange;
  font-size: 35px;
  margin: 3%;
  padding: 2%;
}
.slick-bag__button {
  font-size: 30px;
  background: #f2f2f2;
}
</style>
