<template>
  <div v-if="isChooseCourse" class="container">
    <div class="desk">講台</div>
    <div class="seat-table">
      <div
        v-for="(foo, index) in seatDetails"
        :key="index"
        class="seats"
        :style="getSeatColor(foo.status)"
        @click="chooseSeat(foo.seat_id)"
        @mouseenter="showSeat($event, foo.seat_id)"
        @mouseleave="leaveSeat"
      ></div>
      <div id="hoverBox" v-show="showHover">
        <div class="hoverText">{{ hoverInfo }}</div>
      </div>
    </div>
    <div class="legend">
      <div class="legend-box">
        <div v-for="(foo, index) in legend" :key="index">
          <div class="seats" :style="getSeatColor(foo.status)"></div>
          <div class="legend-text">
            {{ foo.value }}
          </div>
        </div>
      </div>
      <div class="btn" :class="{ active: isChoose }" @click="finishChoose">
        {{ btnText }}
      </div>
    </div>
  </div>
  <div v-else class="seat-text">請選擇課程與日期</div>
</template>

<script>
import { getCourse, bookSeat, cancelBookedSeat } from "@/api";
export default {
  name: "SeatTable",
  props: {
    isChooseCourse: {
      type: Boolean,
      default: false,
    },
    course_id: {
      type: String,
      default: "",
    },
    course_date: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      courseData: [],
      seatDetails: [],
      legend: [
        { status: 0, value: "已預約" },
        { status: 1, value: "可預約" },
        { status: 2, value: "已選取" },
      ],
      isChoose: false,
      btnText: "完成選取",
      selectedSeat: null,
      canBook: true,
      showHover: false,
      hoverInfo: "",
    };
  },
  methods: {
    getSeats(course) {
      this.courseData = [];
      this.seatDetails = [];
      this.selectedSeat = null;
      this.isChoose = false;
      this.canBook = true;
      getCourse(course.course_id, course.date).then((res) => {
        if (res.status == 200) {
          this.courseData = res.data.data;
          console.log(this.courseData);
          let margin = 32 / this.courseData.numberPerRow;
          document.documentElement.style.setProperty(`--space`, margin + "%");
          let i;
          for (i = 0; i < this.courseData.totalSeat; i++) {
            this.seatDetails.push({
              seat_id: i,
              status: 1,
              info: [],
            });
          }
          for (i = 0; i < this.courseData.seats.length; i++) {
            let seat_id = this.courseData.seats[i].seat_id;
            let user_id = this.courseData.seats[i].reserved_by;
            this.seatDetails[seat_id].info.push({
              reserved_by: user_id,
              name: this.courseData.seats[i].name,
            });
            if (user_id == this.$store.state.ID) {
              this.seatDetails[seat_id].status = 2;
              this.selectedSeat = seat_id;
              this.btnText = "取消預約";
              this.isChoose = true;
              this.canBook = false;
            } else {
              this.seatDetails[seat_id].status = 0;
            }
          }
        }
      });
    },
    getSeatColor(status) {
      if (status == 0) {
        return "background-color: #c4c4c4";
      } else if (status == 1) {
        return "background-color: #18a0fb";
      } else {
        return "background-color: #fb5c18";
      }
    },
    chooseSeat(seat_id) {
      if (this.canBook == true) {
        if (this.seatDetails[seat_id].status == 1) {
          // can be reserved
          this.seatDetails[seat_id].status = 2;
          if (this.selectedSeat != null) {
            this.seatDetails[this.selectedSeat].status = 1;
            this.selectedSeat = null;
          }
          this.isChoose = true;
          this.selectedSeat = seat_id;
          this.btnText = "完成選取";
        } else if (this.seatDetails[seat_id].status == 0) {
          // cannot be reserved
          if (
            this.seatDetails[this.selectedSeat].info.reserved_by ==
            this.$store.state.ID
          ) {
            this.seatDetails[seat_id].status = 0;
            this.canBook = false;
          }
        }
      }
    },
    finishChoose() {
      if (this.$store.state.ID == "") {
        this.$store.commit("setLogin", true);
        // this.getSeats({ course_id: this.course_id, date: this.course_date });
        this.$emit("update");
      } else {
        if (this.canBook == false) {
          cancelBookedSeat(
            this.course_id,
            this.course_date,
            this.selectedSeat,
            this.$store.state.ID
          );
          this.seatDetails[this.selectedSeat].status = 1;
          this.selectedSeat = null;
          this.btnText = "完成選取";
          this.isChoose = false;
          this.canBook = true;
        } else {
          bookSeat(
            this.course_id,
            this.course_date,
            this.selectedSeat,
            this.$store.state.ID
          );
          this.seatDetails[this.selectedSeat].status = 2;
          this.seatDetails[this.selectedSeat].info.push({
            reserved: this.$store.state.ID,
            name: this.$store.state.name,
          });
          this.btnText = "取消預訂";
          this.canBook = false;
        }
      }
    },
    showSeat(event, seat_id) {
      this.hoverInfo = "";
      if (this.seatDetails[seat_id].status == 0) {
        this.showHover = true;
        this.hoverInfo = this.seatDetails[seat_id].info[0].name;
      } else if (this.seatDetails[seat_id].status == 1) {
        this.showHover = true;
        this.hoverInfo = "可預約";
      } else if (this.seatDetails[seat_id].status == 2) {
        if (
          this.seatDetails[seat_id].info[0].reserved_by == this.$store.state.ID
        ) {
          this.hoverInfo = "你的座位";
        } else {
          this.hoverInfo = "目前選擇";
        }
      }
      var showDiv = document.getElementById("hoverBox");
      // var seatBox = document.getElementsByClassName("seat-table");

      // let overW = seatBox.getBoundingClientRect().width;
      // let overH = seatBox.getBoundingClientRect().height;
      // let overs = {
      //   x: seatBox.scrollWidth - seatBox.clientWidth,
      //   y: seatBox.scrollHeight - seatBox.clientHeight,
      // };
      // let x = window.pageXOffset + event.clientX - this.offsetLeft;
      // let y = window.pageYOffset + event.clientY - this.offsetTop;
      // seatBox.scrollLeft = (x / overW) * overs.x;
      // seatBox.scrollTop = (y / overH) * overs.y;

      showDiv.style.left = event.pageX - 180 + "px";
      showDiv.style.top = event.pageY - 280 + "px";
      showDiv.style.display = "block";
    },
    leaveSeat() {
      this.showHover = false;
    },
  },
};
</script>
<style lang="scss" scoped>
:root {
  --space: 1em;
}
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  .desk {
    position: absolute;
    background-color: #c4c4c4;
    top: 5%;
    width: 90%;
    height: 6%;
    padding: 0.4%;
    text-align: center;
  }
  .seat-table {
    position: absolute;
    flex: none;
    width: 90%;
    height: 70%;
    overflow: auto;
    display: flex;
    flex-wrap: wrap;
    margin: 6% 10%;
    justify-content: space-between;
    .seats {
      flex: none;
      position: relative;
      margin: 1em var(--space);
      height: 1em;
      width: 1em;
      padding: 2%;
      border-radius: 0.2em;
      .status0 {
        background-color: #c4c4c4;
      }
      .status1 {
        background-color: #18a0fb;
      }
      .status2 {
        background-color: #fb5c18;
      }
    }
    #hoverBox {
      position: absolute;
      z-index: 9999;
      min-width: 4em;
      padding: 0.3em;
      height: 2em;
      border-radius: 0.2em;
      background-color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      filter: drop-shadow(4px 4px 4px rgba(0, 0, 0, 0.2));
      .hoverText {
        text-align: center;
        font-size: 0.8rem;
        padding: 0.1rem;
      }
    }
  }
  .legend {
    position: absolute;
    bottom: 0%;
    width: 100%;
    z-index: 9;
    display: flex;
    align-items: center;
    .legend-box {
      width: 65%;
      height: 5%;
      display: flex;
      flex-direction: row;
      margin: 2% 7%;
      justify-content: space-between;
      align-items: center;
      div {
        flex: auto;
        display: flex;
        align-items: center;
        margin-right: 5%;
        .seats {
          flex: none;
          padding: 10%;
          width: 10%;
          border-radius: 0.2em;
        }
        .legend-text {
          position: relative;
          flex: none;
          font-size: 0.8rem;
        }
      }
    }
    .btn {
      right: 10%;
      width: 15%;
      height: 5%;
      background-color: #c4c4c4;
      &.active {
        transition: 0.3s;
        background-color: #fb5c18;
        color: #ffffff;
        filter: drop-shadow(4px 4px 4px rgba(0, 0, 0, 0.2));
      }
    }
  }
}
.seat-text {
  display: inline-block;
  font-family: "Montserrat";
  font-style: normal;
  margin: auto 0;
  font-weight: 500;
  font-size: 1.2em;
  align-items: center;
  text-align: center;
  color: #555555;
}
</style>
