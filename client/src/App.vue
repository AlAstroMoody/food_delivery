<template>
  <div id="app">
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header";

export default {
  name: "app",
  components: { Header }
};
</script>

<style>
#app {
  background-color: #f2f2f2;
  line-height: 1;
  margin: 0;
  padding: 0;
  font-family: Roboto, FreeSans, sans-serif;
  min-width: 960px;
  color: #000;
  -webkit-text-size-adjust: none;
}
</style>
