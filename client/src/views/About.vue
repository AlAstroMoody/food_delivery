<template>
  <section class="about">
    <transition name="boom" appear>
      <box-for-info class="about__info">
        <template v-slot:header>
          <h2><i class="el-icon-dish-1" />Домашняя итальянская кухня</h2>
        </template>
        <p>
          Мы заботимся о качестве наших блюд, поэтому тщательно подбираем
          подходящие ингредиенты. Тесто для пиццы и паст готовится вручную по
          классическим итальянским рецептам.
        </p>
      </box-for-info>
    </transition>
    <transition name="boom2" appear>
      <box-for-info class="about__info">
        <template v-slot:header>
          <h2><i class="el-icon-cold-drink" />Коктейли и домашние напитки</h2>
        </template>
        <p>
          Вкуснейшие домашние холодные и горячие напитки, алкогольные коктейли,
          шоты, а также коллекция крепких напитков и вин, прекрасно сочетающихся
          с блюдами нашего меню.
        </p>
      </box-for-info>
    </transition>
    <transition name="boom3" appear>
      <box-for-info class="about__info">
        <template v-slot:header>
          <h2>
            <i class="el-icon-table-lamp" />Хороший вкус и теплая атмосфера
          </h2>
        </template>
        <p>
          Майк и Молли уделили большое внимание созданию уютной атмосферы. Это
          простой и стильный интерьер, приятное обслуживание и, что немаловажно,
          у нас не курят!
        </p>
      </box-for-info>
    </transition>
  </section>
</template>

<script>
import BoxForInfo from "@/components/boxForInfo";
export default {
  name: "About",
  components: { BoxForInfo }
};
</script>

<style scoped>
.about {
  width: 80%;
  max-width: 1000px;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-content: flex-start;
  margin: 0 auto;
}

.about__info {
  width: 45%;
  min-width: 300px;
  max-width: 500px;
  font-size: 20px;
  line-height: 1.38;
  color: #484848;
  margin: auto;
  text-align: left;
}

h2 {
  font-weight: 100;
  font-size: 40px;
  line-height: 1.38;
}

.boom-enter-active {
  animation: slideInLeft 2s;
}
.boom2-enter-active {
  animation: slideInRight 3s;
}
.boom3-enter-active {
  animation: slideInLeft 4s;
}

@keyframes slideInLeft {
  from {
    transform: translate(-1800px);
  }
  to {
    transform: translate(0px);
  }
}
@keyframes slideInRight {
  from {
    transform: translate(3600px);
  }
  to {
    transform: translate(0px);
  }
}
@keyframes slideInLeft {
  from {
    transform: translate(-3600px);
  }
  to {
    transform: translate(0px);
  }
}
.el-icon-dish-1 {
  color: green;
  margin-left: -40px;
}

.el-icon-cold-drink {
  color: green;
  margin-left: -40px;
}

.el-icon-table-lamp {
  color: green;
  margin-left: -40px;
}
</style>
