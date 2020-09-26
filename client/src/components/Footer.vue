<template>
  <div class="footer">
    <div class="footer__info">
      <p>© 2020. ООО «Рога и копыта».</p>
      <p>
        Информация на сайте носит справочный характер и не является публичной
        офертой.
      </p>
      <p>
        Внешний вид, цена и состав блюд могут отличаться от представленных на
        сайте.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
.footer {
  height: 25vh;
  min-height: 230px;
  width: 100%;
  padding: 30px 0 30px;
  background-color: #e5e5e5;
  box-shadow: 4px -2px 10px 0 rgba(0, 0, 0, 0.1);
}
.footer__info {
  display: flex;
  flex-direction: column;
  margin-left: 5%;
  width: 80%;
  text-align: left;
}
</style>
