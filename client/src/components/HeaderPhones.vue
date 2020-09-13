<template>
  <div class="phone">
    <span class="phone__text">{{ title }}</span>
    <span class="phone__number">
      <i class="el-icon-knife-fork" v-if="!delivery">{{ phone }} </i>
      <transition name="boom" appear>
        <i class="el-icon-truck" v-if="delivery" />
      </transition>
      <template v-if="delivery">{{ phone }} </template>
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
  display: flex;
  font-size: 25px;
  min-width: 150px;
  color: white;
}

.boom-enter-active {
  animation: slideIn 5s;
}

@keyframes slideIn {
  from {
    transform: translate(-800px);
  }
  to {
    transform: translate(0px);
  }
}
</style>
