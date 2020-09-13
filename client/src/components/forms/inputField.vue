<template>
  <div class="field">
    <label for="field" class="field__label"> {{ name }} </label>
    <el-input id="field" class="field__input" v-model="editField" />
  </div>
</template>

<script>
export default {
  name: "inputField",
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
  width: 30%;
  min-width: 140px;
}
.field__input {
  width: 65%;
  min-width: 190px;
}
</style>
