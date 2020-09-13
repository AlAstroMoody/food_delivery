<template>
  <div class="authorization">
    <h2>{{ title }}</h2>
    <div class="authorization__body">
      <el-input
        class="authorization__login"
        placeholder="логин"
        v-model="editLogin"
      />
      <i v-if="!loginValid" class="authorization__error">
        {{ loginErrorInfo }}
      </i>
      <el-input
        class="authorization__password"
        placeholder="пароль"
        v-model="editPassword"
      />
      <i v-if="!passwordValid" class="authorization__error">
        {{ passwordErrorInfo }}
      </i>
      <el-input
        v-if="!auth"
        class="authorization__password"
        placeholder="подтвердите пароль"
        v-model="editSecondPassword"
      />
      <i v-if="!passwordSecondValid & !auth" class="authorization__error">
        {{ passwordSecondErrorInfo }}
      </i>
    </div>
    <div>
      <el-button
        round
        type="success"
        @click="signIn"
        :disabled="!loginValid || !passwordValid || !passwordSecondValid"
      >
        {{ buttonTitle }}
      </el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthOrRegister",
  data() {
    return {
      login: "",
      password: "",
      passwordRepeat: "",
      loginValid: true,
      passwordValid: true,
      passwordSecondValid: true
    };
  },
  props: {
    title: {
      type: String,
      default: ""
    },
    buttonTitle: {
      type: String,
      default: ""
    },
    auth: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    editLogin: {
      get() {
        return this.login;
      },
      set(login) {
        this.login = login;
        this.validateLogin(login);
      }
    },
    editPassword: {
      get() {
        return this.password;
      },
      set(password) {
        this.password = password;
        this.validatePassword(password);
      }
    },
    editSecondPassword: {
      get() {
        return this.passwordRepeat;
      },
      set(password) {
        this.passwordRepeat = password;
        this.validateSecondPassword(password);
      }
    }
  },
  methods: {
    validateLogin(login) {
      if (login.length < 4) {
        this.loginValid = false;
        this.loginErrorInfo = "В логине должен быть от 4 до 20 символов";
      } else this.loginValid = true;
      if (/^[a-zA-Z1-9а-яА-ЯёЁ_.+-@]+$/.test(login) === false) {
        this.loginValid = false;
        this.loginErrorInfo =
          "В логине должны быть только буквы, цифры и символы @/./+/-/_";
      }
    },
    validatePassword(password) {
      if (password.length < 6) {
        this.passwordValid = false;
        this.passwordErrorInfo = "В пароле должен быть от 6 до 20 символов";
      } else this.passwordValid = true;
    },
    validateSecondPassword(password) {
      if (password !== this.password) {
        this.passwordSecondValid = false;
        this.passwordSecondErrorInfo = "Пароли должны совпадать";
      } else this.passwordSecondValid = true;
    },
    signIn() {
      if (this.login && this.password) {
        let formData = new FormData();
        formData.set("username", this.login);
        formData.set("password", this.password);
        this.$emit("signIn", formData);
      }
    }
  }
};
</script>

<style scoped>
.authorization__body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.authorization__login {
  margin: 1%;
}
.authorization__password {
  margin: 1%;
}
.authorization__error {
  font-size: 15px;
  text-align: left;
  color: red;
}
</style>
