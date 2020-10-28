<template>
  <yandex-map :coords="coords" :zoom="zoom" class="map">
    <ymap-marker :coords="coords" marker-id="123" :hint-content="title" />
    <ymap-marker
      v-for="zone in zones"
      :key="zone.title"
      :marker-id="zone.title"
      :coords="zone.coords"
      marker-type="polyline"
      :hint-content="zone.title"
      :marker-stroke="{ color: zone.color, width: 5 }"
    />
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
      default: "Майк и Молли"
    },
    zones: {
      type: Array,
      default: () => []
    },
    zoom: {
      type: Number,
      default: 15
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
