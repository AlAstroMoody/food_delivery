<template>
  <div id="app">
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";

export default {
  name: "app",
  components: { Header, Footer }
};
</script>

<style>
#app {
  background-color: #f2f2f2;
  line-height: 1;
  margin: 0;
  padding: 0;
  /*font-family: Roboto, FreeSans, sans-serif;*/
  color: #000;
  -webkit-text-size-adjust: none;
}
</style>
