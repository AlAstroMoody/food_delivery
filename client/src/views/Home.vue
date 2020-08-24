<template>
  <div class="home">
    <Cafe />
    <section class="home__main">
      <div class="slick-bag">
        оформить заказ
      </div>
      Тут будет меню
      <div v-for="dish in dishes" :key="dish.id" class="home__menu">
        <DishCard :dish="dish" />
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
import Cafe from "../components/Cafe";
import DishCard from "../components/DishCard";
import Footer from "../components/Footer";
export default {
  name: "Home",
  components: { Cafe, DishCard, Footer },
  created() {}
};
</script>
<style scoped>
.home {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.home__main {
  display: flex;
  width: 80%;
}
.slick-bag {
  width: 20%;
}
.home__menu {
  display: flex;
  width: 80%;
  flex-wrap: wrap;
}
</style>
