<template>
  <div class="phone">
    <span class="phone__text">{{ title }}</span>
    <span class="phone__number">
      <i class="el-icon-knife-fork" v-if="!delivery" />
      <i class="el-icon-truck" v-if="delivery" />
      {{ phone }}
    </span>
  </div>
</template>

<script>
export default {
  name: "HeaderPhones",
  props: {
    phone: {
      type: String,
      default: ""
    },
    title: {
      type: String,
      default: ""
    },
    delivery: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped>
.phone {
  display: flex;
  flex-direction: column;
  margin-left: 3%;
  justify-content: flex-end;
}
.phone__text {
  text-align: center;
  font-size: 15px;
}

.phone__number {
  font-size: 30px;
  display: flex;
  color: white;
}
</style>
