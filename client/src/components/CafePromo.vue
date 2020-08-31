<template>
  <el-card class="cafe-promo" :body-style="{ padding: '0px' }">
    <el-carousel indicator-position="outside">
      <el-carousel-item
        v-for="image in images"
        :key="image"
        class="cafe-promo__container"
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
  border-radius: 10px;
}
.cafe-promo__container {
  display: flex;
  justify-content: center;
}
.cafe-promo__image {
  width: 100%;
  height: auto;
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}
@media screen and (max-width: 960px) {
  .cafe-promo__image {
    top: 30%;
  }
}
</style>
