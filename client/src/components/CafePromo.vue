<template>
  <el-card class="cafe-promo">
    <el-carousel indicator-position="outside" class="cafe-promo__carousel">
      <el-carousel-item
        v-for="image in images"
        :key="image"
        class="cafe-promo__carousel-item"
      >
        <img :src="image" />
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
  },
  created() {
    console.log(this.images);
  }
};
</script>

<style scoped>
.cafe-promo {
  width: 70%;
  height: 100%;
  border-radius: 3%;
}

.cafe-promo__carousel-item {
  font-size: 18px;
  line-height: 300px;
  margin: 0;
  width: 100%;
}
</style>
