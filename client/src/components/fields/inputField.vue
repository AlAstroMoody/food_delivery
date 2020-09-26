<template>
  <div class="field">
    <label for="field" class="field__label"> {{ name }} </label>
    <el-input
      id="field"
      class="field__input"
      v-model="editField"
      :class="isError"
    />
  </div>
</template>

<script>
export default {
  name: "inputField",
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
  width: 30%;
  min-width: 140px;
}

.field__input {
  width: 65%;
  min-width: 190px;
}

.error {
  outline: 1px solid red;
}
</style>
