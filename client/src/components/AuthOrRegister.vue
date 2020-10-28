<template>
  <div class="authorization">
    <h2>{{ title }}</h2>
    <div class="authorization__body">
      <el-input
        class="authorization__login"
        placeholder="логин"
        v-model="editLogin"
        :class="!loginValid ? 'error' : ''"
      />
      <i v-if="!loginValid" class="authorization__error">
        {{ loginErrorInfo }}
      </i>
      <el-input
        class="authorization__password"
        placeholder="пароль"
        v-model="editPassword"
        :class="!passwordValid ? 'error' : ''"
      />
      <i v-if="!passwordValid" class="authorization__error">
        {{ passwordErrorInfo }}
      </i>
      <el-input
        v-if="!auth"
        class="authorization__password"
        placeholder="подтверждение пароля"
        v-model="editSecondPassword"
        :class="!passwordSecondValid ? 'error' : ''"
      />
      <i v-if="!passwordSecondValid & !auth" class="authorization__error">
        {{ passwordSecondErrorInfo }}
      </i>
    </div>
    <div>
      <el-button round type="success" @click="signIn" :disabled="disabled">
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
    disabled() {
      return (
        !this.loginValid ||
        !this.passwordValid ||
        !this.passwordSecondValid ||
        !this.login ||
        !this.password ||
        (!this.passwordRepeat && !this.auth)
      );
    },
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

.error {
  outline: 2px solid red;
  animation-name: shakeError;
  animation-fill-mode: forwards;
  animation-duration: 600ms;
  animation-timing-function: ease-in-out;
}

@keyframes shakeError {
  0% {
    transform: translateX(0);
  }
  15% {
    transform: translateX(0.375rem);
  }
  30% {
    transform: translateX(-0.375rem);
  }
  45% {
    transform: translateX(0.375rem);
  }
  60% {
    transform: translateX(-0.375rem);
  }
  75% {
    transform: translateX(0.375rem);
  }
  90% {
    transform: translateX(-0.375rem);
  }
  100% {
    transform: translateX(0);
  }
}
</style>
