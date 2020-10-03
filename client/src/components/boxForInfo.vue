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
  name: "boxForInfo"
};
</script>

<style scoped>

footer {
  display: flex;
  width: 100%;
}
</style>
