<template>
  <div>
    <div class="Mask" v-if="this.$store.state.isLogin == true"></div>
    <div class="menu">
      <h2 class="menu-text">Seat Reservaion System</h2>
      <button @click.once="Sign" id="login" type="button" class="btn btn-light">
        登入
      </button>
      <button id="register" type="button" class="btn btn-dark">註冊</button>
    </div>
    <div class="body">
      <div class="option-menu">
        <h2 class="text">請選擇課程:</h2>
        <select class="lesson-select" v-model="LessonName">
          <option value="軟體工程">軟體工程 (4201-64人)</option>
          <option value="資料庫系統">資料庫系統 (4203-64人)</option>
        </select>
        <h2 class="date-text">請選擇日期:</h2>
        <select class="date-select" v-model="LessonTime">
          <option value="2022/03/29">2022/03/29</option>
          <option value="2022/04/05">2022/04/05</option>
        </select>
      </div>
      <div class="option-menu">
        <h2 class="text">教室位置圖</h2>
      </div>
      <div class="seat">
        <div class="seat-text">請選擇課程與日期</div>
      </div>
    </div>
    <div class="win" v-if="this.$store.state.isLogin == true">
      <SignPopup></SignPopup>
    </div>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery";
import "bootstrap/dist/js/bootstrap.min.js";
import SignPopup from "./SignPopup.vue";
export default {
  name: "Function_Bar",
  data() {
    return {
      LessonName: "請選擇課程名稱:",
      LessonTime: "請選擇課程日期:",
    };
  },
  methods: {
    Sign() {
      this.$store.commit("setLogin", true);
    },
  },
  components: {
    SignPopup,
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
}
.Mask {
  position: absolute;
  z-index: 100;
  top: 8%;
  width: 100%;
  height: 92%;
  background: #000000;
  opacity: 0.6;
}

.body {
  position: absolute;
  width: 100%;
  height: 92%;
  left: 0px;
  top: 8%;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  .option-menu {
    position: relative;
    left: 5%;
    top: 4%;
    width: 90%;
    height: 10%;
    display: flex;
    flex-direction: row;
    align-items: center;
    .text {
      width: 15%;
      position: relative;
      left: 1%;
      top: 7%;
      font-family: "Montserrat";
      font-style: normal;
      font-weight: 500;
      font-size: 24px;
      line-height: 29px;
      text-align: center;
      letter-spacing: -0.015em;
      color: #000000;
    }
    .lesson-select {
      width: 25%;
      height: 50%;
    }
    .date-text {
      width: 15%;
      position: relative;
      left: 10%;
      top: 7%;
      font-family: "Montserrat";
      font-style: normal;
      font-weight: 500;
      font-size: 24px;
      line-height: 29px;
      text-align: center;
      letter-spacing: -0.015em;
      color: #000000;
    }
    .date-select {
      position: relative;
      left: 10%;
      width: 25%;
      height: 50%;
      padding-left: 7.5%;
    }
  }
  .seat {
    position: relative;
    width: 80%;
    height: 70%;
    color: black;
    position: absolute;
    left: 7.5%;
    top: 22.5%;
    bottom: 0%;
    background: #f0f0f0;
    border-radius: 5px;
    .seat-text {
      position: relative;
      left: 42.52%;
      right: 42.6%;
      top: 47.86%;
      bottom: 47.86%;

      font-family: "Montserrat";
      font-style: normal;
      font-weight: 500;
      font-size: 24px;
      line-height: 29px;
      display: flex;
      align-items: center;
      text-align: center;
      letter-spacing: -0.015em;

      color: #555555;
    }
  }
}
.win {
  border: 0px;
  padding: 0px;
  position: absolute;
  width: 45.5%;
  height: 51%;
  left: 27.5%;
  top: 150px;
  z-index: 600;
  background-color: white;
}
</style>
