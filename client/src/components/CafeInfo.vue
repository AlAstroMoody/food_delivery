<template>
  <div class="cafe-info">
    <span class="cafe-info__block-about">
      <i class="el-icon-knife-fork" />
      Мы — это <a href="/about/">уютное кафе</a> итальянской домашней кухни в
      центре города
    </span>
    <span class="cafe-info__block-map">
      <i class="el-icon-location" />
      Наш адрес:
      <div class="cafe-info__address-link">
        <a href="/map/?department=1"> ул.&nbsp;Диктатуры пролетариата, 32а</a>
      </div>
      <div class="cafe-info__address-link">
        <a href="/map/?department=2">ул.&nbsp;Партизана Железняка, 26а</a>
      </div>
    </span>
    <span class="cafe-info__block-delivery">
      <i class="el-icon-truck" />
      <a href="/delivery/">Время работы и условия доставки</a>
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
@media screen and (max-width: 1080px) {
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
