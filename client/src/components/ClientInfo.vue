<template>
  <div class="client-info">
    <form class="client-info__form">
      <input-field
        name="Как вас зовут?"
        :value.sync="profile.name"
        :pattern="/^[a-zA-Zа-яА-Я]{2,30}$/"
      />
      <input-field
        name="Номер телефона"
        :value.sync="profile.phone"
        :pattern="/^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7}$/"
      />
      <text-area-field name="Комментарий к заказу" :value.sync="comment" />
      <el-switch
        v-model="delivery"
        active-color="#13ce66"
        inactive-color="#0088ff"
        active-text="Доставка"
        inactive-text="Самовывоз"
        class="client-info__switch"
        :width="60"
      >
      </el-switch>
      <transition name="fade" mode="out-in">
        <input-field
          v-if="delivery"
          name="Адрес доставки:"
          :value.sync="profile.address"
          :pattern="/./"
        />
        <select-field
          v-if="!delivery"
          name="Адрес самовывоза:"
          :options="options"
          @returnValue="returnPlace"
        />
      </transition>
      <el-button
        type="primary"
        @click="onSubmit"
        class="client-info__button"
        :disabled="!formValid"
      >
        Сделать заказ
      </el-button>
    </form>
  </div>
</template>

<script>
import inputField from "@/components/forms/inputField";
import TextAreaField from "@/components/forms/textAreaField";
import SelectField from "@/components/forms/selectField";
import { CENTER, VZLETKA } from "@/api/const";
export default {
  name: "ClientInfo",
  data() {
    return {
      comment: "",
      delivery: true,
      place: "",
      options: [CENTER, VZLETKA]
    };
  },
  computed: {
    profile() {
      return this.$store.state.profile;
    },
    formValid() {
      return (
        this.profile.name &&
        this.profile.phone &&
        (this.profile.address || this.place)
      );
    }
  },
  components: {
    SelectField,
    TextAreaField,
    inputField
  },
  methods: {
    returnPlace(address) {
      this.place = address;
    },
    onSubmit() {
      // прикрутить валидацию
      let formData = new FormData();
      formData.set("user", this.$store.state.token.user.pk);
      formData.set("status", 1);
      formData.set("comment", this.comment);
      formData.set("user_name", this.profile.name);
      formData.set("phone", this.profile.phone);
      if (this.delivery) {
        formData.set("is_delivery", true);
        formData.set("address", this.profile.address);
      } else {
        formData.set("is_delivery", false);
        console.log(this.place);
        formData.set("address", this.place);
      }
      this.$emit("createOrder", formData);
    }
  }
};
</script>

<style scoped>
.client-info {
  display: flex;
  flex-direction: column;
  font-size: 20px;
  font-weight: 100;
  margin: 0 5px;
}

.client-info__form {
  display: flex;
  flex-direction: column;
  margin: 2%;
}

.client-info__switch {
  margin: auto;
  padding: 10px;
}

.client-info__button {
  margin: auto;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
