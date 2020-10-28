<template>
  <div id="app">
    <the-header />
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
    <the-footer />
  </div>
</template>

<script>
import TheFooter from "@/components/layout/TheFooter";
import TheHeader from "@/components/layout/TheHeader";

export default {
  name: "app",
  components: { TheHeader, TheFooter }
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
  display: flex;
  flex-direction: column;
}

a {
  text-decoration: none;
  font-weight: 500;
  color: #409eff;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
