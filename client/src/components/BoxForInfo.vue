<template>
  <div class="container">
    <header>
      <slot name="header"></slot>
    </header>
    <main>
      <slot></slot>
    </main>
    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<script>
export default {
  name: "BoxForInfo"
};
</script>

<style scoped>
main {
  width: 100%;
}
footer {
  display: flex;
  width: 100%;
}
</style>
