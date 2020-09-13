<template>
  <div class="home">
    <about-cafe class="home__cafe" />
    <transition name="fade">
      <modal-dish
        v-if="modalVisible"
        @showModal="showModal"
        :dish="dish"
        class="home__modal-dish"
      />
    </transition>
    <section class="home__main">
      <slick-bag
        class="home__slick-bag"
        :order="order"
        @removeDishInOrder="removeDishInOrder"
        @addToOrder="addToOrder"
        @decreaseQuantityInOrder="decreaseQuantityInOrder"
      />
      <section class="home__menu">
        <div v-for="dish in dishes" :key="dish.id" class="home__menu-cards">
          <dish-card
            :dish="dish"
            @addToOrder="addToOrder"
            @showModal="showModal"
          />
        </div>
      </section>
    </section>
  </div>
</template>

<script>
import AboutCafe from "../components/AboutCafe";
import DishCard from "../components/DishCard";
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
  components: { AboutCafe, DishCard, SlickBag, ModalDish },
  methods: {
    ...mapActions([
      "editOrder",
      "removeDishInOrder",
      "decreaseQuantityInOrder",
      "getAllDishes"
    ]),
    showModal(dish) {
      this.modalVisible = !this.modalVisible;
      this.dish = dish;
    },
    addToOrder(id) {
      this.$store.dispatch("editOrder", this.getDishById(id));
    },
    removeDishInOrder(id) {
      this.$store.dispatch("removeDishInOrder", this.getDishById(id));
    },
    decreaseQuantityInOrder(id) {
      this.$store.dispatch("decreaseQuantityInOrder", this.getDishById(id));
    },
    getDishById(id) {
      for (let i = 0; i < this.dishes.length; i++) {
        if (this.dishes[i]["id"] === id) {
          return {
            id: id,
            name: this.dishes[i]["name"],
            price: this.dishes[i]["price"]
          };
        }
      }
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
.home__slick-bag {
  width: 20%;
  height: 100%;
  min-height: 300px;
  border-radius: 10%;
  position: sticky;
  min-width: 300px;
  top: 0;
  left: 15%;
}
.home__menu {
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  width: 60%;
  flex-wrap: wrap;
}
.home__menu-cards {
  display: flex;
  width: 30%;
  min-width: 190px;
  margin-bottom: 2%;
}
.home__modal-dish {
  display: flex;
  justify-content: center;
  align-items: center;
}
@media screen and (max-width: 1370px) {
  .home__menu {
    width: 80%;
    justify-content: flex-end;
  }
  .home__slick-bag {
    left: 5%;
  }
}
@media screen and (max-width: 960px) {
  .home__menu {
    width: 100%;
    justify-content: center;
  }
  .home__slick-bag {
    display: none;
  }
}
.home__cafe {
  width: 80%;
}
.fade-enter {
  opacity: 0;
}
.fade-enter-active {
  transition: opacity 0.4s;
}
.fade-leave-active {
  transition: opacity 0.4s;
}
.fade-leave-to {
  opacity: 0;
}
</style>
