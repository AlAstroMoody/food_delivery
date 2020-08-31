<template>
  <el-form :inline="true" ref="form" :model="form">
    <label for="name">Как вас зовут?</label>
    <el-input v-model="form.name" id="name"></el-input>
    <div class="input-group">
      <label for="phone">Телефон: </label>
      <el-input
        v-model="form.phone"
        id="phone"
        placeholder="+7(555) 555-5555"
        autocomplete="tel"
        maxlength="11"
      />
    </div>

    <label for="desc"> Комментарий к заказу </label>
    <el-input type="textarea" v-model="form.desc" id="desc"></el-input>

    <el-tabs type="border-card">
      <el-tab-pane>
        <span slot="label"><i class="el-icon-truck" /> Доставка </span>
        Компонент с доставкой
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label"><i class="el-icon-dish-1" /> Cамовывоз </span>
        Компонент с самовывозом
      </el-tab-pane>
    </el-tabs>
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
        desc: "",
        phone: ""
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
