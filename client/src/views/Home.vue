<template>
  <div class="home">
    <div class="home__filters">
      <el-button
        type="text"
        v-for="category in categories"
        :key="category.id"
        class="home__filters-button"
        @click="filteredDishes(category.id)"
        :class="{ 'home__filters-active': idCategory === category.id }"
      >
        {{ category.name }}
      </el-button>
      <el-input v-model="query" placeholder="поиск" />
    </div>
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
      <transition-group name="fade" class="home__menu">
        <div
          v-for="dish in queryDishes"
          :key="dish.id"
          class="home__menu-cards"
        >
          <dish-card
            :dish="dish"
            @addToOrder="addToOrder"
            @showModal="showModal"
          />
        </div>
      </transition-group>
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
      dish: {},
      query: "",
      idCategory: -1
    };
  },
  components: { AboutCafe, DishCard, SlickBag, ModalDish },
  methods: {
    ...mapActions([
      "editOrder",
      "removeDishInOrder",
      "decreaseQuantityInOrder"
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
    },
    filteredDishes(id) {
      if (this.idCategory !== id) {
        this.idCategory = id;
      } else this.idCategory = -1;
    }
  },
  computed: {
    dishes() {
      return this.$store.state.dishes;
    },
    categories() {
      return this.$store.state.categories;
    },
    order() {
      return this.$store.state.order;
    },
    queryDishes() {
      if (this.idCategory > -1) {
        return this.dishes.filter(item => {
          return (
            item.category === this.idCategory &&
            item.name.toLowerCase().indexOf(this.query.toLowerCase()) !== -1
          );
        });
      } else
        return this.dishes.filter(item => {
          return (
            item.name.toLowerCase().indexOf(this.query.toLowerCase()) !== -1
          );
        });
    }
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

.home__filters {
  display: flex;
  width: 60%;
  background: white;
  border-radius: 10px;
  padding: 5px;
  position: sticky;
  top: 0;
  z-index: 20;
  border: 1px solid #e5e5e5;
  margin-top: -5px;
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
  max-width: 400px;
  top: 60px;
  left: 15%;
}

.home__menu {
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  width: 60%;
  margin-left: 5%;
  flex-wrap: wrap;
}

.home__menu-cards {
  display: flex;
  width: 30%;
  min-width: 190px;
  min-height: 200px;
  max-width: 300px;
  margin: 1%;
}

.home__modal-dish {
  display: flex;
  justify-content: center;
  align-items: center;
}

@media screen and (max-width: 1600px) {
  .home__menu {
    width: 80%;
    justify-content: flex-end;
    margin: auto;
  }
  .home__slick-bag {
    left: 10%;
  }
}
@media screen and (max-width: 1400px) {
  .home__menu {
    width: 100%;
    justify-content: center;
    margin-left: 5%;
  }
  .home__slick-bag {
    left: 5%;
  }
  .home__menu-cards {
    min-width: 250px;
  }
  .home__filters {
    display: none;
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.home__filters-button {
  font-size: 16px;
  margin: 3px;
  padding: 3px;
}

.home__filters-button:hover {
  background: #adcc52;
  color: white;
  transition: color 0.5s;
}

.home__filters-active {
  background: #adcc52;
  color: white;
  transition: color 0.5s;
}
</style>
