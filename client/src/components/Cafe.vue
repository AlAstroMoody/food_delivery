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
  name: "Cafe",
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
    ...mapActions(["getPromoImages"])
  },
  created() {
    this.$store.dispatch("getPromoImages");
  }
};
</script>

<style scoped>
.cafe {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 1%;
  height: auto;
}
.cafe__info {
  width: 30%;
  min-width: 300px;
}
.cafe__promo {
  width: 60%;
  min-width: 380px;
}
@media screen and (max-width: 1080px) {
  .cafe__info {
    width: 100%;
    min-width: 600px;
  }
  .cafe__promo {
    width: 80%;
    height: auto;
  }
}

@media screen and (max-width: 600px) {
  .cafe__info {
    display: none;
  }
  .cafe__promo {
    max-height: 200px;
  }
}
</style>
