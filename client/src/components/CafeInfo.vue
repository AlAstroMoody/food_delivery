<template>
  <div class="cafe-info">
    <span class="cafe-info__block-about">
      Мы — это <a href="/about/">уютное кафе</a> итальянской домашней кухни в
      центре города
    </span>
    <span class="cafe-info__block-map">
      Наш адрес:
      <div class="cafe-info__address-link">
        <a href="/map/?department=1"> ул.&nbsp;Диктатуры пролетариата, 32а</a>
      </div>
      <div class="cafe-info__address-link">
        <a href="/map/?department=2">ул.&nbsp;Партизана Железняка, 26а</a>
      </div>
    </span>
    <span class="cafe-info__block-delivery">
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
  margin: 15px 20px 0 0;
  width: 286px;
  text-align: left;
  font-size: 19px;
  font-weight: 300;
  line-height: 1.21;
  padding-left: 46px;
  position: relative;
}
</style>
