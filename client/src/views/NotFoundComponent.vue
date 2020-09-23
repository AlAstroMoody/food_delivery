<template>
  <div class="not-found">
    <h1 class="not-found__title">Такой страницы не существует</h1>
    <img class="not-found__img" src="../assets/404.gif" alt="travolta" />
  </div>
</template>

<script>
export default {
  name: "NotFoundComponent"
};
</script>

<style scoped>
.not-found {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.not-found__title {
  height: 100px;
}
</style>
