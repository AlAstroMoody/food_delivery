<template>
  <div class="home">
    <Cafe />
    <ModalDish v-if="modalVisible" @showModal="showModal" :dish="dish" />
    <section class="home__main">
      <SlickBag
        class="slick-bag"
        :order="order"
        :dishes="dishes"
        @removeDishInOrder="removeDishInOrder"
        @addToOrder="addToOrder"
        @decreaseQuantityInOrder="decreaseQuantityInOrder"
      />
      <section class="home__menu">
        <div v-for="dish in dishes" :key="dish.id" class="home__menu-cards">
          <DishCard
            :dish="dish"
            @addToOrder="addToOrder"
            @showModal="showModal"
          />
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
import ModalDish from "../components/ModalDish";
import { mapActions } from "vuex";
export default {
  name: "Home",
  data() {
    return {
      modalVisible: false,
      dish: {}
    };
  },
  components: { Cafe, DishCard, Footer, SlickBag, ModalDish },
  methods: {
    ...mapActions([
      "getAllDishes",
      "editOrder",
      "removeDishInOrder",
      "decreaseQuantityInOrder"
    ]),
    addToOrder(id) {
      this.$store.dispatch("editOrder", id);
    },
    removeDishInOrder(id) {
      this.$store.dispatch("removeDishInOrder", id);
    },
    showModal(dish) {
      this.modalVisible = !this.modalVisible;
      this.dish = dish;
    },
    decreaseQuantityInOrder(id) {
      this.$store.dispatch("decreaseQuantityInOrder", id);
    }
  },
  computed: {
    dishes() {
      return this.$store.state.dishes;
    },
    order() {
      return this.$store.state.order;
    }
  },
  created() {
    this.$store.dispatch("getAllDishes");
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
  width: 100%;
  justify-content: space-evenly;
}
.slick-bag {
  width: 20%;
  border-radius: 10%;
  position: sticky;
  top: 0;
}
.home__menu {
  display: flex;
  width: 70%;
  flex-wrap: wrap;
}
.home__menu-cards {
  display: flex;
  width: 30%;
  margin-bottom: 5%;
}
</style>
