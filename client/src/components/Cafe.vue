<template>
  <div class="cafe">
    <CafeInfo class="cafe__info" />
    <CafePromo :images="promoImages" class="cafe__promo" />
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
  height: 60%;
}
@media screen and (max-width: 1080px) {
  .cafe__info {
    width: 100%;
    min-width: 600px;
  }
}
@media screen and (max-width: 960px) {
  .cafe__promo {
    max-height: 200px;
  }
}
@media screen and (max-width: 600px) {
  .cafe__info {
    display: none;
  }
}
</style>
