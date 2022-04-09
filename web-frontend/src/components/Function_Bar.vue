<template>
  <div>
    <transition name="fade">
      <div class="Mask" v-if="this.$store.state.isLogin == true">
        <SignPopup class="win" :isSignup="Is_SignUp"></SignPopup>
      </div>
    </transition>
    <div class="menu">
      <h2 class="menu-text">Seat Reservaion System</h2>
      <button
        v-if="this.$store.state.name == ''"
        @click="Sign"
        id="login"
        type="button"
        class="btn btn-light"
      >
        登入
      </button>
      <button
        v-if="this.$store.state.name == ''"
        @click="Sign_up"
        id="register"
        type="button"
        class="btn btn-dark"
      >
        註冊
      </button>
      <span class="user-info" v-if="this.$store.state.name != ''"
        >您好，{{ this.$store.state.name }}({{ this.$store.state.ID }}) &nbsp;
        <a href="#" @click="Sign_out">登出</a></span
      >
    </div>
    <div class="body">
      <div class="option-menu">
        <h2 class="text">請選擇課程：</h2>
        <select
          class="lesson-select"
          v-model="LessonName"
          @click="ShowLesson"
          @change="ChooseLesson"
        >
          <option
            v-for="Course in CourseList"
            :value="Course.name"
            :key="Course.name"
          >
            {{ Course.name + "   ( " + Course.classroom + " )" }}
          </option>
        </select>
        <h2 class="date-text">請選擇日期：</h2>
        <select class="date-select" v-model="LessonTime">
          <option
            v-for="Date in DateList"
            :value="Date"
            :key="Date"
            @click="ChooseDate"
          >
            {{ Date }}
          </option>
        </select>
      </div>
      <div class="option-menu">
        <h2 class="text">教室位置圖</h2>
      </div>
      <div class="seat">
        <SeatTable :isChooseCourse="Is_ChooseCourse" />
      </div>
    </div>
    <!--<div class="win" v-if="this.$store.state.isLogin == true">
      <SignPopup></SignPopup>
    </div>
    -->
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery";
import "bootstrap/dist/js/bootstrap.min.js";
import SignPopup from "./SignPopup.vue";
import SeatTable from "./SeatReserve.vue";
// import { getAllCourse } from "@/api";

export default {
  name: "Function_Bar",
  data() {
    return {
      LessonName: "請選擇課程名稱:",
      LessonTime: "請選擇課程日期:",
      Is_SignUp: false,
      CourseSelect: false,
      TimeSelect: false,
      CourseList: [
        {
          id: "ALGO",
          name: "演算法",
          classroom: "65405",
          date: ["2022-04-01", "2022-04-08"],
        },
        {
          id: "NASA",
          name: "計算機網路",
          classroom: "65304",
          date: ["2022-04-07"],
        },
        {
          id: "SW",
          name: "軟體工程",
          classroom: "4201",
          date: ["2022-03-31", "2022-04-05"],
        },
      ],
      DateList: [],
      Is_ChooseCourse: false,
    };
  },
  methods: {
    Sign() {
      this.$store.commit("setLogin", true);
      this.Is_SignUp = false;
    },
    Sign_up() {
      this.$store.commit("setLogin", true);
      this.Is_SignUp = true;
    },
    Sign_out() {
      var i = "";
      var n = "";
      this.$store.commit("setUserInformation", { i, n });
    },
    async ShowLesson() {
      const response = await fetch("/course/getAllCourse");
      const res = await response.json();
      var i, j;
      for (j = 0; this.CourseList.length != 0; j++) {
        this.CourseList.pop();
      }
      for (i = 0; i < res.data.length; i++) {
        this.CourseList.push({
          id: res.data[i].id,
          name: res.data[i].name,
          classroom: res.data[i].classroom,
          date: res.data[i].date,
        });
      }
      this.CourseSelect = true;
    },
    ChooseLesson() {
      var i, j, k;
      // pop all element in array
      for (k = 0; this.DateList.length != 0; k++) {
        this.DateList.pop();
      }
      // mutex
      while (this.LessonName[0] == "請") {
        continue;
      }
      for (i = 0; i < this.CourseList.length; i++) {
        if (this.LessonName == this.CourseList[i].name) {
          for (j = 0; j < this.CourseList[i].date.length; j++) {
            this.DateList.push(this.CourseList[i].date[j]);
          }
        }
      }
      this.TimeSelect = true;
      if (this.CourseSelect == true && this.TimeSelect == true) {
        this.Is_ChooseCourse = true;
      } else {
        this.Is_ChooseCourse = false;
      }
    },
  },
  components: {
    SignPopup,
    SeatTable,
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

  span {
    position: relative;
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
    left: 62.5%;
    color: #555555;
  }
}
.Mask {
  position: absolute;
  z-index: 100;
  top: 8%;
  width: 100%;
  height: 92%;
  background: rgb(0, 0, 0, 0.6);
  //opacity: 0.6;
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
  background-color: white;
  //opacity: 1;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
</style>
