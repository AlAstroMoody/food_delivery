<template>
  <el-card class="cafe-promo" :body-style="{ padding: '0px' }">
    <el-carousel indicator-position="outside" class="cafe-promo__carousel">
      <el-carousel-item
        v-for="image in images"
        :key="image"
        class="cafe-promo__carousel-item"
      >
        <img :src="image" class="cafe-promo__image" />
      </el-carousel-item>
    </el-carousel>
  </el-card>
</template>

<script>
export default {
  name: "CafePromo",
  props: {
    images: {
      type: Array,
      default: () => []
    }
  }
};
</script>

<style scoped>
.cafe-promo {
  width: 80%;
  height: 100%;
  border-radius: 3%;
}

.cafe-promo__carousel-item {
  font-size: 18px;
  line-height: 300px;
  margin: 0;
  width: 100%;
}
.cafe-promo__image {
  width: 100%;
}
</style>
