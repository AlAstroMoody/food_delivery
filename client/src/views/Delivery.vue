<template>
  <box-for-info class="delivery">
    <template v-slot:header>
      <h2>Условия доставки</h2>
    </template>
    <p>
      Мы доставляем наши вкусные блюда по Красноярску
      <strong>совершенно бесплатно. </strong>
    </p>
    <p>ПН-ЧТ c 11:00 до 22:30,</p>
    <p>ПТ c 11:00 до 23:30,</p>
    <p>СБ c 12:00 до 23:30,</p>
    <p>ВС c 12:00 до 22:30.</p>

    <p>
      Минимальная сумма заказа зависит от вашего местоположения:
    </p>
    <div class="delivery__zone">
      <div>
        <span class="delivery__zone-green"> Зеленая зона </span>
        <p>Заказ от 490,-</p>
      </div>
      <div>
        <span class="delivery__zone-blue">Синяя зона </span>
        <p>Заказ от 590,-</p>
      </div>
      <div>
        <span class="delivery__zone-yellow">Желтая зона </span>
        <p>Заказ от 790,-</p>
      </div>
      <div>
        <span class="delivery__zone-red"> Красная зона </span>
        <p>Заказ от 1290,–</p>
      </div>
    </div>
    <template v-slot:footer>
      <yandex-map class="delivery__map" />
    </template>
  </box-for-info>
</template>

<script>
import BoxForInfo from "@/components/boxForInfo";
import YandexMap from "@/components/YandexMap";

export default {
  name: "Delivery",
  components: { YandexMap, BoxForInfo }
};
</script>

<style scoped>
.delivery {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 50%;
  min-width: 360px;
  margin: 10px auto;
  border-radius: 10px;
  background: white;
  padding: 20px;
  font-size: 20px;
}

h2 {
  font-weight: 100;
  font-size: 40px;
}

span {
  min-width: 100px;
  width: 19%;
  margin: 20px;
}

strong {
  color: #fc9221;
}

.delivery__zone {
  display: flex;
  flex-wrap: wrap;
  text-align: center;
  justify-content: center;
}

.delivery__map {
  margin: 0 auto;
  min-width: 350px;
  width: 100%;
  height: 500px;
}

.delivery__zone div {
  border: 1px solid #e5e5e5;
  width: 22%;
  min-width: 170px;
  margin: 1%;
}

.delivery__zone-green {
  color: green;
}

.delivery__zone-red {
  color: red;
}

.delivery__zone-blue {
  color: blue;
}

.delivery__zone-yellow {
  color: #ffd800;
}
</style>
