<template>
  <div class="header-social">
    <el-button class="header-social__button" type="text" circle>
      <img src="../../assets/social_facebook.png" alt="fb" />
    </el-button>
    <el-button class="header-social__button" type="text" circle>
      <img src="../../assets/social_instagram.png" alt="instagram" />
    </el-button>
    <el-button class="header-social__button" type="text" circle>
      <img src="../../assets/social_vk.png" alt="vk" />
    </el-button>
    <el-button class="header-social__button" type="text" circle>
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
  position: relative;
  padding: 0;
}

.header-social__button:hover {
  background: white;
  transition: background 0.5s;
}

.header-social__button:after {
  content: "";
  width: 30px;
  height: 30px;
  position: absolute;
  left: calc(50% - 15px);
  top: calc(50% - 15px);
  border-radius: 0 50% 50% 50%;
  box-shadow: 0 0 3px 1px rgba(0, 0, 0, 0.3);
}
</style>
