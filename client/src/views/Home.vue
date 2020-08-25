<template>
  <div class="home">
    <Cafe />
    <section class="home__main">
      <SlickBag class="slick-bag" />
      <section class="home__menu">
        <div v-for="dish in dishes" :key="dish.id" class="home__menu-cards">
          <DishCard :dish="dish" />
        </div>
      </section>
    </section>
    <Footer />
  </div>
</template>

<script>
import Cafe from "../components/Cafe";
import DishCard from "../components/DishCard";
import Footer from "../components/Footer";
import SlickBag from "../components/SlickBag";
import { mapActions } from "vuex";
export default {
  name: "Home",
  components: { Cafe, DishCard, Footer, SlickBag },
  methods: {
    ...mapActions(["getAllDishes"])
  },
  computed: {
    dishes() {
      return this.$store.state.dishes;
    }
  },
  created() {
    this.$store.dispatch("getAllDishes");
    console.log(this.dishes);
  }
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
  max-height: 300px;
  border-radius: 10%;
}
.home__menu {
  display: flex;
  width: 80%;
  flex-wrap: wrap;
  justify-content: space-around;
}
.home__menu-cards {
  display: flex;
  width: 30%;
  margin-bottom: 5%;
}
</style>
