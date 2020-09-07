<template>
  <div class="field">
    <label for="field" class="field__label"> {{ name }} </label>
    <el-date-picker
      v-model="editField"
      type="date"
      placeholder="Выберите дату"
      default-value="2000-01-01"
      value-format="yyyy-MM-dd"
      id="field"
      class="field__input"
    >
    </el-date-picker>
  </div>
</template>

<script>
export default {
  name: "dataField",
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
        this.$emit("returnValue", value);
      }
    }
  }
}
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
