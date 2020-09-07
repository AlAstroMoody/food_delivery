<template>
  <el-menu class="header" mode="horizontal">
    <div class="header__content">
      <div class="header__phones">
        <header-phones
          title="Телефон доставки"
          phone="226-65-65"
          :delivery="true"
        />
        <HeaderPhones title="Заказ столиков" phone="261-01-65" />
      </div>
      <div class="header__logo-container">
        <img class="header__logo-img" src="../assets/logo.png" alt="logo" />
        <span class="header__logo-title">cafe &amp; bar</span>
      </div>
      <header-social class="header__social" />
    </div>
    <el-tag v-if="Username" class="header__user" effect="dark" type="success">
      <span>
        <i class="el-icon-user" />
        <router-link :to="{ name: 'Profile' }"> {{ Username }} </router-link>
      </span>
      <el-divider direction="vertical"></el-divider>
      <el-link @click="Logout">
        <span>Logout</span>
      </el-link>
    </el-tag>
    <div class="header__empty"></div>
  </el-menu>
</template>

<script>
import HeaderPhones from "./HeaderPhones";
import HeaderSocial from "./HeaderSocial";
export default {
  name: "Header",
  components: {
    HeaderPhones,
    HeaderSocial
  },
  computed: {
    Username() {
      return this.$store.state.token.user.username;
    }
  },
  methods: {
    Logout() {
      this.$store.dispatch("logout");
      this.$notify({
        title: "Вы вышли из акаунта",
        type: "info"
      });
    }
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
  width: 70%;
  margin: 0 auto;
  height: 94px;
  position: relative;
}
.header__phones {
  display: flex;
  width: 30%;
}
.header__logo-container {
  width: 40%;
  max-width: 277px;
}
.header__logo-img {
  background: url(../assets/logo.png) no-repeat;
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
  margin-left: -70px;
  letter-spacing: 1px;
  display: block;
  left: 50%;
  position: absolute;
}

.header__social {
  display: flex;
  position: relative;
  width: 30%;
  height: 30%;
  margin-top: 5%;
  justify-content: center;
}

.header__user {
  position: absolute;
  right: 10px;
  top: 30px;
  margin-right: 20px;
  font-size: 17px;
}
@media screen and (max-width: 1370px) {
  .header__content {
    width: 100%;
  }
  .header__user {
    display: none;
  }
}
@media screen and (max-width: 960px) {
  .header__phones {
    display: none;
  }
  .header__social {
    display: none;
  }
  .header__logo-container {
    width: 100%;
  }
  .header__content {
    height: 50px;
  }
  .header__logo-img {
    top: 10%;
  }
}
</style>
