<template>
  <div class="menu">
    <h2 class="menu-text">Seat Reservaion System</h2>
    <button id="login" type="button" class="btn btn-light">登入</button>
    <button id="register" type="button" class="btn btn-dark">註冊</button>
  </div>
</template>

<script>
export default {
  name: "Function_Bar",
  data() {
    return {};
  },
  methods: {
    goOff() {
      if (this.destination == "0") {
        this.$router.go(-1);
      } else if (this.destination == "reload") {
        this.reload();
      } else {
        this.$router.push({ name: this.destination });
      }
    },
    goProfile() {
      this.$router.push("/profile");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.menu {
  position: absolute;
  width: 100%;
  height: 8%;
  left: 0px;
  top: 0px;
  display: flex;
  flex-direction: row;

  background: #f0f0f0;
  box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.2);
}
.menu-text {
  position: relative;
  width: 250px;
  height: 29px;
  left: 2.5%;
  top: 20%;

  font-family: "Montserrat";
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 29px;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: -0.015em;

  color: #555555;
}

button {
  position: relative;
  width: 65px;
  height: 29px;
  top: 20%;
  font-family: "Montserrat";
  font-style: normal;
  font-weight: 600;
  font-size: 15.5px;
  line-height: 22px;
  /* identical to box height */

  display: flex;
  align-items: center;
  text-align: center;
}

#login {
  left: 62.5%;
  color: #555555;
}

#register {
  left: 65%;
  color: #ffffff;
}
</style>
