<template>
  <div class="delivery">
    <el-button
      round
      @click="place = center"
      class="delivery__button-first"
      :class="{ 'delivery__button-active': place === center }"
    >
      ул. Диктатуры пролетариата, 32А
    </el-button>
    <el-button
      round
      @click="place = vzletka"
      :class="{ 'delivery__button-active': place === vzletka }"
      class="delivery__button-second"
    >
      ул. Партизана Железняка, 26А
    </el-button>
    <yandex-map :coords="place.coords" :title="place.title" />
  </div>
</template>

<script>
import YandexMap from "@/components/YandexMap";
export default {
  name: "Map",
  data() {
    return {
      center: {
        title: "Майк и молли на Диктатуры",
        coords: [56.011975, 92.8589]
      },
      vzletka: {
        title: "Майк и молли на Партизана",
        coords: [56.031275, 92.9179]
      },
      place: ""
    };
  },
  components: { YandexMap }
};
</script>

<style scoped>
.delivery {
  width: 100%;
  height: 610px;
  position: relative;
}
.delivery__button-first {
  position: absolute;
  right: 5px;
  top: 1%;
  z-index: 999;
}

.delivery__button-second {
  position: absolute;
  right: 5px;
  top: 12%;
  z-index: 999;
}

.delivery__button-active {
  background: orange;
  color: white;
}
</style>
