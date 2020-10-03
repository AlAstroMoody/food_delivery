<template>
  <div class="profile">
    <h1>Личный кабинет</h1>
    <el-card class="profile__card">
      <form class="client-info__form">
        <input-field
          name="Как вас зовут?"
          :value.sync="profile.name"
          :pattern="/^[a-zA-Zа-яА-Я]{2,30}$/"
        />
        <input-field
          name="Номер телефона"
          :value.sync="profile.phone"
          :pattern="/^[0-9]{11}$/"
        />
        <input-field
          name="E-mail"
          :value.sync="profile.email"
          :pattern="/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/"
        />
        <input-field name="Адрес доставки:" :value.sync="profile.address" />
        <data-field name="Дата рождения" :value.sync="profile.birthday" />
        <el-button type="primary" @click="onSubmit">
          Сохранить
        </el-button>
      </form>
    </el-card>
  </div>
</template>

<script>
import inputField from "@/components/fields/inputField";
import dataField from "@/components/fields/dataField";
import { CENTER, VZLETKA } from "@/api/const";
import { mapActions } from "vuex";

export default {
  name: "Profile",
  data() {
    return {
      options: [CENTER, VZLETKA]
    };
  },
  components: {
    inputField,
    dataField
  },
  computed: {
    profile() {
      return this.$store.state.profile;
    }
  },
  methods: {
    ...mapActions(["getUserProfile", "editUserProfile"]),
    onSubmit() {
      let formData = new FormData();
      formData.set("user", this.$store.state.token.user.pk);
      formData.set("name", this.profile.name);
      formData.set("address", this.profile.address);
      formData.set("phone", this.profile.phone);
      if (this.profile.birthday) {
        formData.set("birthday", this.profile.birthday);
      }
      if (this.profile.email) {
        formData.set("email", this.profile.email);
      }
      this.$store.dispatch("editUserProfile", formData);
      this.$notify.success({
        message: "Изменения сохранены!"
      });
    }
  },
  async created() {
    await this.getUserProfile(this.$store.state.token.user.pk);
  }
};
</script>

<style scoped>
.profile {
  height: 500px;
  text-align: center;
}
.profile__card {
  width: 50%;
  min-width: 550px;
  max-width: 700px;
  margin: auto;
  text-align: left;
}
@media screen and (max-width: 600px) {
  .profile__card {
    min-width: 380px;
  }
  .client-info__form {
    display: flex;
    flex-direction: column;
  }
}
</style>
