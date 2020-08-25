<template>
  <div class="cafe">
    <CafeInfo />
    <CafePromo :images="promoImages" />
  </div>
</template>

<script>
import CafeInfo from "./CafeInfo";
import CafePromo from "./CafePromo";
export default {
  name: "Cafe",
  data() {
    return {
      //  брать из api как доделаю его
      promoImages: [
        "http://127.0.0.1:8000/media/promo/dr.png",
        "http://127.0.0.1:8000/media/promo/mikedowntown.png"
      ]
    };
  },
  components: {
    CafeInfo,
    CafePromo
  }
};
</script>

<style scoped>
.cafe {
  display: flex;
  width: 60%;
  margin: 1%;
}
</style>
