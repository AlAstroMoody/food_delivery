<template>
  <el-menu class="header" mode="horizontal">
    <div class="header__content">
      <div class="header__phones">
        <HeaderPhones
          title="Телефон доставки"
          phone="226-65-65"
          :delivery="true"
        />
        <HeaderPhones title="Заказ столиков" phone="261-01-65" />
      </div>
      <div class="header__logo-container">
        <img class="header__logo-img" src="../assets/logo.png" />
        <span class="header__logo-title">cafe &amp; bar</span>
      </div>
      <div class="header__social">
        <el-button class="header__social-button">
          <img src="../assets/social_facebook.png" />
        </el-button>
        <el-button class="header__social-button">
          <img src="../assets/social_instagram.png" />
        </el-button>
        <el-button class="header__social-button">
          <img src="../assets/social_vk.png" />
        </el-button>
        <el-button class="header__social-button">
          <img src="../assets/social_twitter.png" />
        </el-button>
      </div>
      <div class="header__cart"></div>
    </div>
    <div class="header__empty"></div>
  </el-menu>
</template>

<script>
import HeaderPhones from "./HeaderPhones";
export default {
  name: "Header",
  components: {
    HeaderPhones
  }
};
</script>

<style scoped>
.header {
  display: flex;
  background: #adcc52;
  box-shadow: 4px 2px 10px 0 rgba(0, 0, 0, 0.1);
  justify-content: center;
  flex-wrap: wrap;
}

.header__empty {
  width: 100%;
  background-size: 10px 10px;
  border-top: 1px solid #739900;
  height: 20px;
  background: #adcc52;
}

.header__content {
  display: flex;
  justify-content: space-around;
  text-align: start;
  width: 1170px;
  margin: 0 auto;
  height: 94px;
  position: relative;
}
.header__phones {
  display: flex;
}
.header__logo-img {
  background: url(../assets/logo.png) no-repeat;
  width: 277px;
  height: 75px;
  filter: drop-shadow(1px 1px 0 #8ba442);
  top: 50%;
  position: absolute;
}
.header__logo-title {
  height: 13px;
  background: #adcc52;
  padding: 0 10px 10px;
  font-size: 20px;
  color: #739900;
  bottom: -21px;
  margin-left: -53px;
  letter-spacing: 1px;
  display: block;
  left: 50%;
  position: absolute;
}

.header__logo-container {
  width: 277px;
}

.header__social {
  display: flex;
  position: relative;
  height: 30%;
  margin-top: 5%;
  justify-content: flex-end;
}
.header__social-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  padding: 0;
  background: #c4f197;
}
</style>
