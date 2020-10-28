<template>
  <span>{{ displayNumber }} ₽ </span>
</template>

<script>
export default {
  name: "AnimatedNumber",
  props: {
    number: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      displayNumber: this.number,
      interval: false
    };
  },
  watch: {
    number() {
      clearInterval(this.interval);
      if (this.number === this.displayNumber) {
        return;
      }
      this.interval = window.setInterval(
        function() {
          if (this.displayNumber !== this.number) {
            let change = (this.number - this.displayNumber) / 10;
            change = change >= 0 ? Math.ceil(change) : Math.floor(change);
            this.displayNumber = this.displayNumber + change;
          }
        }.bind(this),
        10
      );
    }
  }
};
</script>

<style scoped></style>
