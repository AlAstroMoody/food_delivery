<template>
  <el-card class="cafe-promo" :body-style="{ padding: '0px' }">
    <el-carousel indicator-position="outside">
      <el-carousel-item
        v-for="image in images"
        :key="image.id"
        class="cafe-promo__container"
      >
        <img :src="image.image" class="cafe-promo__image" />
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
  border-radius: 10px;
}
.cafe-promo__container {
  display: flex;
}
.cafe-promo__image {
  width: 100%;
  margin: auto;
  position: relative;
  top: -8%;
}

@media screen and (max-width: 600px) {
  .cafe-promo__image {
    position: relative;
    top: -20%;
  }
}
</style>
