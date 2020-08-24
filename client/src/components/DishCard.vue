<template>
  <el-card class="dish">
    тут будет карточка блюда
  </el-card>
</template>

<script>
export default {
  name: "DishCard",
  props: {
    dish: {
      type: Array,
      default: () => []
    }
  }
};
</script>

<style scoped>
.dish {
  display: flex;
  min-width: 200px;
  min-height: 300px;
}
</style>
