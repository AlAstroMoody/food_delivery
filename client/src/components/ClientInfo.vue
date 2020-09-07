<template>
  <div class="client-info">
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
      <text-area-field
        name="Комментарий к заказу"
        :value="comment"
        @returnText="returnComment"
      />
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
      <input-field
        v-show="delivery"
        name="Адрес доставки:"
        :value="profile.address"
        @returnValue="returnAddress"
      />
      <select-field
        v-show="!delivery"
        name="Адрес самовывоза:"
        :options="options"
        @returnValue="returnPlace"
      />
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
      delivery: "",
      place: "",
      formValid: true,
      options: [CENTER, VZLETKA]
    };
  },
  computed: {
    profile() {
      return this.$store.state.profile;
    }
  },
  components: {
    SelectField,
    TextAreaField,
    inputField
  },
  methods: {
    returnComment(comment) {
      this.comment = comment;
    },
    returnName(name) {
      this.profile.name = name;
    },
    returnPhone(phone) {
      this.profile.phone = phone;
    },
    returnAddress(address) {
      this.profile.address = address;
    },
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
</style>
