<template>
  <div class="cafe-info">
    <span class="cafe-info__block-about">
      <i class="el-icon-knife-fork" />
      Мы — это
      <router-link :to="{ name: 'About' }">уютное кафе</router-link> итальянской
      домашней кухни в центре города
    </span>
    <div class="cafe-info__block-map">
      <i class="el-icon-location" />
      Наш адрес:
      <div class="cafe-info__address-link">
        <router-link :to="{ name: 'Map' }">
          ул. Диктатуры пролетариата, 32а
        </router-link>
      </div>
      <div class="cafe-info__address-link">
        <router-link :to="{ name: 'Map' }">
          ул. Партизана Железняка, 26а
        </router-link>
      </div>
    </div>
    <span class="cafe-info__block-delivery">
      <i class="el-icon-truck" />
      <router-link :to="{ name: 'Delivery' }">
        Время работы и условия доставки
      </router-link>
    </span>
  </div>
</template>

<script>
export default {
  name: "CafeInfo"
};
</script>

<style scoped>
.cafe-info {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  text-align: left;
  font-size: 20px;
  line-height: 1.21;
  padding: 20px;
}

@media screen and (max-width: 1440px) {
  .cafe-info {
    flex-direction: row;
    text-align: center;
  }
  .cafe-info__block-about {
    width: 30%;
  }
  .cafe-info__block-map {
    width: 35%;
  }
  .cafe-info__block-delivery {
    width: 30%;
  }
}
</style>
