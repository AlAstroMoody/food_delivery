<template>
  <label class="field">
    <span class="field__label">{{ name }} </span>
    <el-input type="textarea" class="field__input" v-model="editField" />
  </label>
</template>

<script>
export default {
  name: "TextAreaField",
  props: {
    name: {
      type: String,
      default: "title"
    },
    value: {
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
  min-width: 140px;
}
.field__input {
  width: 50%;
  min-width: 130px;
}
</style>
