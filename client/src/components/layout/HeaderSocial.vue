<template>
  <div class="header-social">
    <el-button class="header-social__button">
      <img src="../../assets/social_facebook.png" alt="fb" />
    </el-button>
    <el-button class="header-social__button">
      <img src="../../assets/social_instagram.png" alt="instagram" />
    </el-button>
    <el-button class="header-social__button">
      <img src="../../assets/social_vk.png" alt="vk" />
    </el-button>
    <el-button class="header-social__button">
      <img src="../../assets/social_twitter.png" alt="twitter" />
    </el-button>
  </div>
</template>

<script>
export default {
  name: "HeaderSocial"
};
</script>

<style scoped>
.header-social__button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  padding: 0;
  background: #c4f197;
}
</style>
