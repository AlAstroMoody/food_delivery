<template>
  <div class="client-info">
    <div class="client-info__name-phone">
      <div>
        <label for="name">Как вас зовут?</label>
        <el-input v-model="name" id="name"></el-input>
      </div>
      <div class="input-group">
        <label for="phone">Телефон: </label>
        <el-input
          v-model="phone"
          id="phone"
          placeholder="+7(555) 555-5555"
          autocomplete="tel"
          maxlength="11"
        />
      </div>
    </div>

    <label for="comment"> Комментарий к заказу </label>
    <el-input type="textarea" v-model="comment" id="comment"></el-input>
    <div class="client-info__delivery">
      <el-switch
        style="display: block"
        v-model="delivery"
        active-color="#13ce66"
        inactive-color="#0088ff"
        active-text="Доставка"
        inactive-text="Самовывоз"
        class="client-info__delivery-switch"
      >
      </el-switch>
      <label for="address" v-if="delivery">Адрес доставки:</label>
      <el-input v-model="getAddress" id="address" v-if="delivery"></el-input>
      <div>
        <label for="select" v-if="!delivery">Адрес самовывоза:</label>
        <el-select
          v-model="getAddress"
          placeholder="Select"
          v-if="!delivery"
          class="client-info__address-select"
        >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            id="select"
          >
          </el-option>
        </el-select>
      </div>
    </div>
    <div>
      <el-button type="primary" @click="onSubmit">Сделать заказ</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ClientInfo",
  data() {
    return {
      name: "",
      comment: "",
      phone: "",
      address: "",
      delivery: "",
      options: [
        {
          value: "Москва, Красная площадь, Кремль",
          label: "Москва, Красная площадь, Кремль"
        },
        {
          value: "Красноярск, под Октябрьским мостом",
          label: "Красноярск, под Октябрьским мостом"
        }
      ],
      value: ""
    };
  },
  computed: {
    getAddress: {
      get() {
        return this.address;
      },
      set(address) {
        this.address = address;
      }
    }
  },
  methods: {
    onSubmit() {
      // прикрутить валидацию
      let formData = new FormData();
      formData.set("user", this.$store.state.token.user.pk);
      formData.set("status", 1);
      formData.set("comment", this.comment);
      formData.set("user_name", this.name);
      formData.set("phone", this.phone);
      if (this.delivery) {
        formData.set("is_delivery", true);
        formData.set("address", this.address);
      } else {
        formData.set("is_delivery", false);
        formData.set("address", this.address);
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
  font-size: 25px;
  margin: 0 5px;
}
.client-info__name-phone {
  display: flex;
  justify-content: space-between;
  margin: 1% 0 1% 0;
}
.client-info__delivery {
  margin: 1% 0 1% 0;
}
.client-info__address-select {
  width: 100%;
}
.client-info__delivery-switch {
  margin: 1% 0 2% 0;
}
</style>
