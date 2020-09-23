<template>
  <div class="field">
    <label for="field" class="field__label"> {{ name }} </label>
    <el-select
      v-model="returnAddress"
      placeholder="Select"
      class="field__input"
    >
      <el-option
        v-for="item in options"
        :key="item.value"
        :value="item"
        id="select"
      >
      </el-option>
    </el-select>
  </div>
</template>

<script>
export default {
  name: "selectField",
  data() {
    return {
      address: ""
    };
  },
  props: {
    name: {
      type: String,
      default: "title"
    },
    options: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    returnAddress: {
      get() {
        return this.address;
      },
      set(value) {
        this.address = value;
        this.$emit("returnValue", value);
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
