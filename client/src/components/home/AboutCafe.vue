<template>
  <div class="cafe">
    <cafe-info class="cafe__info" />
    <cafe-promo :images="promoImages" class="cafe__promo" />
  </div>
</template>

<script>
import CafeInfo from "./CafeInfo";
import CafePromo from "./CafePromo";
import { mapActions } from "vuex";
export default {
  name: "AboutCafe",
  components: {
    CafeInfo,
    CafePromo
  },
  computed: {
    promoImages() {
      return this.$store.state.promo;
    }
  },
  methods: {
    ...mapActions(["setPromoImages"])
  },
  created() {
    this.$store.dispatch("setPromoImages");
  }
};
</script>

<style scoped>
.cafe {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 1%;
  height: auto;
}

.cafe__info {
  width: 385px;
}

.cafe__promo {
  width: 900px;
  margin: auto;
}

@media screen and (max-width: 1440px) {
  .cafe__info {
    width: 900px;
    margin: 1% auto;
  }
}
@media screen and (max-width: 960px) {
  .cafe__info {
    width: 700px;
  }
  .cafe__promo {
    width: 700px;
    height: 250px;
  }
}

@media screen and (max-width: 600px) {
  .cafe__info {
    display: none;
  }
  .cafe__promo {
    width: 480px;
    min-width: 370px;
    height: 200px;
  }
}

@media screen and (max-width: 400px) {
  .cafe__promo {
    height: 150px;
  }
}
</style>
