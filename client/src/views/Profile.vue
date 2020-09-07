<template>
  <div class="profile">
    <h1>Личный кабинет</h1>
    <el-card class="profile__card">
      <form class="client-info__form">
        <input-field
          name="Как вас зовут?"
          :value="profile.name"
          :pattern="/^[a-zA-Z ]{2,30}$/"
          @returnValue="returnName"
        />
        <input-field
          name="Номер телефона"
          :value="profile.phone"
          pattern="/^[0-9]{11}$/"
          @returnValue="returnPhone"
        />
        <input-field
          name="E-mail"
          :value="profile.email"
          pattern="/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/"
          @returnValue="returnEmail"
        />
        <input-field
          name="Адрес доставки:"
          :value="profile.address"
          @returnValue="returnAddress"
        />
        <data-field
          name="Дата рождения"
          :value="profile.birthday"
          @returnValue="returnDate"
        />
        <el-button type="primary" @click="onSubmit">
          Сохранить
        </el-button>
      </form>
    </el-card>
  </div>
</template>

<script>
import inputField from "@/components/forms/inputField";
import dataField from "@/components/forms/dataField";
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
    returnName(name) {
      this.profile.name = name;
    },
    returnPhone(phone) {
      this.profile.phone = phone;
    },
    returnAddress(address) {
      this.profile.address = address;
    },
    returnEmail(email) {
      this.profile.email = email;
    },
    returnDate(date) {
      this.profile.birthday = date;
    },
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
  height: 60vh;
  text-align: center;
}
.profile__card {
  width: 50%;
  min-width: 350px;
  margin: auto;
  text-align: left;
}
</style>
