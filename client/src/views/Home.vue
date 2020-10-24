<template>
  <div class="home">
    <div class="home__filters" :class="{ 'home__filters-show': showFilter }">
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
      <div class="home__filters-hidden">
        <hr />
        <el-button type="text">
          <router-link :to="{ name: 'Delivery' }" class="home__filters-button">
            Доставка
          </router-link>
        </el-button>
        <el-button type="text">
          <router-link :to="{ name: 'About' }" class="home__filters-button">
            О нас
          </router-link>
        </el-button>
      </div>
    </div>
    <el-button
      @click="showFilter = !showFilter"
      class="home__drawer"
      icon="el-icon-s-operation"
      type="text"
    />
    <router-link :to="{ name: 'Order' }">
      <el-button
        class="home__cart"
        icon="el-icon-shopping-cart-full"
        type="text"
      />
    </router-link>
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
      <slick-bag class="home__slick-bag" :order="order" />
      <h2 class="home__menu" v-if="queryDishes.length < 1">
        По вашему запросу ничего не найдено!
      </h2>
      <transition-group name="fade" class="home__menu" v-else>
        <div
          v-for="dish in queryDishes"
          :key="dish.id"
          class="home__menu-cards"
        >
          <dish-card
            :dish="dish"
            @addToOrder="addToOrder(dish)"
            @showModal="showModal"
          />
        </div>
      </transition-group>
    </section>
  </div>
</template>

<script>
import AboutCafe from "../components/home/AboutCafe";
import DishCard from "../components/home/DishCard";
import SlickBag from "../components/home/SlickBag";
import ModalDish from "../components/home/ModalDish";

export default {
  name: "Home",
  data() {
    return {
      modalVisible: false,
      dish: {},
      query: "",
      idCategory: -1,
      showFilter: false
    };
  },
  components: { AboutCafe, DishCard, SlickBag, ModalDish },
  methods: {
    showModal(dish) {
      this.modalVisible = !this.modalVisible;
      this.dish = dish;
    },
    addToOrder(dish) {
      this.$store.dispatch("addNewDishToOrder", {
        id: dish.id,
        name: dish.name,
        price: dish.price
      });
    },
    filteredDishes(id) {
      if (this.idCategory !== id) {
        this.idCategory = id;
      } else this.idCategory = -1;
      this.showFilter = !this.showFilter;
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

.home__drawer {
  display: none;
}

.home__cafe {
  width: 80%;
}

.home__cart {
  display: none;
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

.home__filters-hidden {
  display: none;
}

.home__main {
  display: flex;
  width: 100%;
  justify-content: center;
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
  left: 10%;
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
  }

  .home__slick-bag {
    left: 5%;
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
    width: 90%;
  }
}

@media screen and (max-width: 960px) {
  .home__menu {
    width: 100%;
    justify-content: center;
    margin-left: auto;
  }

  .home__slick-bag {
    display: none;
  }

  .home__filters {
    position: fixed;
    top: 10%;
    left: -250px;
    text-align: left;
    flex-direction: column;
    width: 50%;
    max-width: 200px;
    align-content: flex-start;
    transition: left 0.3s linear;
  }

  .home__filters-hidden {
    display: flex;
    flex-direction: column;
  }

  .home__filters-button {
    text-align: left;
  }

  .home__drawer {
    position: fixed;
    display: flex;
    left: 10px;
    top: 10px;
    z-index: 11;
    color: white;
    font-size: 25px;
  }

  .home__cart {
    position: fixed;
    display: flex;
    right: 10px;
    top: 10px;
    z-index: 11;
    color: white;
    font-size: 25px;
  }
}
@media screen and (max-width: 550px) {
  .home__menu-cards {
    width: 48%;
    min-width: 180px;
  }
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

.home__filters-show {
  left: 1%;
}
</style>
