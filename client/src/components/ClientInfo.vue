<template>
  <el-form ref="form" :model="form">
    <label for="name">Как вас зовут?</label>
    <el-input v-model="form.name" id="name"></el-input>

    <label for="desc"> Комментарий к заказу </label>
    <el-input type="textarea" v-model="form.desc" id="desc"></el-input>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: "ClientInfo",
  data() {
    return {
      form: {
        name: "",
        desc: ""
      }
    };
  },
  methods: {
    onSubmit() {
      let formData = new FormData();
      formData.set("user", this.$store.state.token.user.pk);
      formData.set("status", 1);
      formData.set("comments", this.form.desc);
      this.$emit("createOrder", formData);
    }
  }
};
</script>

<style scoped></style>
