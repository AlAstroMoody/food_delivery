<template>
  <label class="field">
    <span class="field__label">{{ name }}</span>
    <el-input
      :placeholder="placeholder"
      class="field__input"
      v-model="editField"
      :class="isError"
    />
  </label>
</template>

<script>
export default {
  name: "TextField",
  data() {
    return {
      isError: ""
    };
  },
  props: {
    name: {
      type: String,
      default: "title"
    },
    value: {
      type: String,
      default: ""
    },
    pattern: {
      default: false
    },
    placeholder: {
      type: String,
      default: ""
    }
  },
  computed: {
    editField: {
      get() {
        return this.value;
      },
      set(value) {
        if (this.pattern) {
          if (!this.pattern.test(value)) {
            this.isError = "error";
          } else this.isError = "";
        }
        this.$emit("update:value", value);
      }
    }
  }
};
</script>

<style scoped>
.field {
  display: flex;
  flex-wrap: wrap;
  text-align: left;
  justify-content: space-between;
  align-items: center;
  margin: 1%;
}

.field__label {
  width: 50%;
  min-width: 130px;
}

.field__input {
  width: 50%;
  min-width: 130px;
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
