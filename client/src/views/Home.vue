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
    <transition name="fade">
      <modal-dish
        v-if="modalVisible"
        @showModal="showModal"
        :dish="dish"
        class="home__modal-dish"
      />
    </transition>
    <section class="home__main">
      <about-cafe class="home__cafe" />
      <div class="home__main-menu">
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
      </div>
    </section>
    <el-backtop />
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

.home__cart {
  display: none;
}

.home__filters {
  display: flex;
  width: 100%;
  background: white;
  padding: 5px;
  position: sticky;
  top: 0;
  z-index: 9;
  border-bottom: 1px solid #e5e5e5;
  justify-content: center;
}

.el-input {
  max-width: 150px;
}

.home__filters-hidden {
  display: none;
}

.home__main {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.home__cafe {
  width: 70%;
  display: flex;
  min-width: 1310px;
  max-width: 1800px;
  margin: 10px auto;
}

.home__main-menu {
  display: flex;
  width: 70%;
  min-width: 1310px;
  max-width: 1800px;
  margin: auto;
  justify-content: space-between;
}

.home__slick-bag {
  width: 350px;
  height: 100%;
  min-height: 300px;
  border-radius: 10%;
  position: sticky;
  top: 60px;
}

.home__menu {
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  width: 950px;
  flex-wrap: wrap;
  margin: auto;
}

.home__menu-cards {
  width: 276px;
  height: 480px;
  margin-left: 38px;
  margin-bottom: 38px;
}

.home__modal-dish {
  display: flex;
  justify-content: center;
  align-items: center;
}

@media screen and (max-width: 1440px) {
  .home__main-menu {
    width: 900px;
    min-width: auto;
  }
  .home__menu-cards {
    margin-left: 20px;
    margin-bottom: 20px;
  }
  .home__slick-bag {
    width: 400px;
  }
  .home__cafe {
    min-width: 900px;
  }
}

@media screen and (max-width: 960px) {
  .home__menu {
    width: 100%;
    justify-content: center;
    margin-left: auto;
  }
  .home__main-menu {
    width: 600px;
  }
  .home__cafe {
    min-width: 600px;
    width: 600px;
  }
  .home__slick-bag {
    display: none;
  }
  .home__filters {
    position: fixed;
    top: 72px;
    left: -250px;
    text-align: left;
    flex-direction: column;
    width: 50%;
    max-width: 200px;
    align-content: flex-start;
    transition: left 0.3s linear;
    border: 1px solid #685252;
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
  .home__menu-cards {
    width: 190px;
    height: 350px;
    margin: 5px 5px 35px auto;
  }
}

@media screen and (max-width: 600px) {
  .home__menu {
    width: 100%;
    justify-content: center;
  }
  .home__cafe {
    min-width: auto;
    width: 480px;
  }
  .home__main-menu {
    width: 480px;
  }
  .home__menu-cards {
    width: 148px;
    height: 250px;
    margin: 5px 5px 27px auto;
  }
}

@media screen and (max-width: 500px) {
  .home__main-menu {
    max-width: 100%;
  }
  .home__cafe {
    width: 100%;
  }
  .home__menu-cards {
    margin: 1%;
    height: auto;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.el-button--text {
  text-align: left;
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
  border-radius: 10px;
}
</style>
