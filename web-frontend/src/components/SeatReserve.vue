<template>
  <div v-if="isChooseCourse" class="container">
    <div class="desk">講台</div>
    <div class="seat-table">
      <div v-for="foo in seatDetails" :key="foo" class="foo.status"></div>
    </div>
    <div class="legend">
      <div v-for="foo in legend" :key="foo" class="foo.status">
        {{ foo.value }}
      </div>
    </div>
    <div class="btn"></div>
  </div>
  <div v-else class="seat-text">請選擇課程與日期</div>
</template>

<script>
// import { getCourse } from "@/api";
export default {
  name: "SeatTable",
  props: {
    isChooseCourse: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isLogin: false,
      courseData: {
        numberPerRow: 6,
        totalSeat: 60,
        seats: [
          {
            seat_id: 5,
            reserved_by: "F74070000",
            name: "陳簽博",
          },
        ],
      },
      seatDetails: [
        {
          status: 0,
          seatDetail: {
            seat_id: 0,
            reserved_by: "F74040000",
            name: "陳簽博",
          },
        },
        {
          status: 1,
          seatDetail: {
            seat_id: 2,
          },
        },
        {
          status: 0,
          seatDetail: {
            seat_id: 2,
            reserved_by: "F74040000",
            name: "陳簽博",
          },
        },
      ],
      legend: [
        { status: "reserved", value: "已預約" },
        { status: "available", value: "可預約" },
        { status: "choose", value: "已選取" },
      ],
    };
  },
  methods: {
    // getSeatTable(course_id, date) {
    //   getCourse({ course_id: course_id, date: date })
    //     .then((res) => {
    //       if (res.status == 200) {
    //         this.courseData = res.data;
    //         let i, j;
    //         for (i = 0; i < this.courseData.totalSeat; i++) {
    //           for (j = 0; j < this.courseData.seats.length; j++) {
    //             if (i == this.courseData.seats[j].seat_id) {
    //               this.seatDetails[i].push({
    //                 status: 0,
    //                 seatDetail: this.courseData.seats[j],
    //               });
    //             } else {
    //               this.seatDetails[i].push({
    //                 status: 1,
    //                 seatDetail: {},
    //               });
    //             }
    //           }
    //         }
    //       }
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
    getSeats() {
      let i, j;
      for (i = 0; i < this.courseData.totalSeat; i++) {
        for (j = 0; j < this.courseData.seats.length; j++) {
          if (i == this.courseData.seats[j].seat_id) {
            this.seatDetails[i].push({
              status: 0,
              seatDetail: this.courseData.seats[j],
            });
          } else {
            console.log(this.courseData.seats);
            this.seatDetails[i].push({
              status: 1,
              seatDetail: {
                seat_id: i,
              },
            });
            console.log(this.seatDetails[i]);
          }
        }
      }
    },
  },
  computed: {
    getSeatColor(status) {
      if (status == 0) {
        return "#c4c4c4";
      } else if (status == 1) {
        return "#18a0fb";
      } else {
        return "#fb5c18";
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  .desk {
    position: absolute;
    background-color: #c4c4c4;
    top: 5%;
    width: 80%;
    height: 6%;
    padding: 0.5%;
    text-align: center;
  }
  .seat-table {
    width: 85%;
    height: 70%;
    display: flex;
    margin: 12% 20%;
    .seats {
      margin: 2%;
      padding: 3%;
      border-radius: 3px;
      background-color: #c4c4c4;
      &available {
        background-color: #18a0fb;
      }
      &choose {
        background-color: #fb5c18;
      }
    }
  }
  .legend {
    position: absolute;
    bottom: 5%;
    display: flex;
    .box {
      margin: 5%;
      padding: 3%;
    }
  }
}
.seat-text {
  display: inline-block;
  font-family: "Montserrat";
  font-style: normal;
  margin: auto 0;
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  align-items: center;
  text-align: center;
  color: #555555;
}
</style>
