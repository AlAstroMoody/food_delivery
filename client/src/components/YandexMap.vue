<template>
  <yandex-map :coords="coords" :zoom="15" class="map">
    <ymap-marker :coords="coords" marker-id="123" :hint-content="title" />
  </yandex-map>
</template>

<script>
import { yandexMap, ymapMarker } from "vue-yandex-maps";
export default {
  name: "YandexMap",
  props: {
    coords: {
      type: Array,
      default: () => [56.011975, 92.8589]
    },
    title: {
      type: String,
      default: ""
    }
  },
  components: { yandexMap, ymapMarker }
};
</script>

<style scoped>
.map {
  width: 100%;
  height: 100%;
}
</style>
