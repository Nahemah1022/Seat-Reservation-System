<template>
  <popup-frame>
    <div class="sign-up-header">
      <span v-if="isSignup">註冊帳號</span>
      <span v-else>登入帳號</span>
    </div>

    <div class="sign-up-content">
      <table>
        <tr v-if="isSignup">
          <td width="25%">
            <label for="name">姓名</label>
          </td>
          <td>
            <input
              type="text"
              id="name"
              placeholder="請輸入名字"
              v-model="Name"
            />
          </td>
        </tr>
        <tr>
          <td>
            <label for="account">學號</label>
          </td>
          <td>
            <input
              @click.once="Clear_text"
              type="text"
              id="account"
              placeholder="請輸入帳號"
              v-model="Account"
            />
          </td>
        </tr>
        <tr>
          <td>
            <label for="password">密碼</label>
          </td>
          <td>
            <input
              type="password"
              id="password"
              placeholder="請輸入密碼"
              v-model="Password"
            />
          </td>
        </tr>
        <tr v-if="isSignup">
          <td>
            <label for="password-twice">確認密碼</label>
          </td>
          <td>
            <input
              type="password"
              id="password-twice"
              placeholder="請再次輸入密碼"
              v-model="Password_twice"
            />
          </td>
        </tr>
      </table>
    </div>
    <div class="button-group">
      <span v-if="Is_alarm" :style="{ color: Alarm_text_color }">{{
        Alarm_text
      }}</span>
      <input @click="Cancel" type="button" value="取消" />
      <input
        @click="Commit_signup"
        v-if="isSignup"
        type="submit"
        value="註冊"
      />
      <input @click="Commit_signin" v-else type="submit" value="登入" />
    </div>
  </popup-frame>
</template>

<script>
import PopupFrame from "./PopupFrame.vue";
export default {
  name: "SignPopup",
  props: {
    isSignup: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      Name: "",
      Account: "",
      Password: "",
      Password_twice: "",
      Is_alarm: false,
      Alarm_text: "",
      timer: "",
    };
  },
  methods: {
    Cancel() {
      this.$store.commit("setLogin", false);
    },
    Commit() {
      if (this.isSignup) {
        this.Commit_signup();
      } else {
        this.Commit_signin();
      }
    },
    Clear_input() {
      this.Name = "";
      this.Account = "";
      this.Password = "";
      this.Password_twice = "";
    },
    async Commit_signup() {
      this.Is_alarm = true;
      if (this.Name == "") {
        this.Alarm_text = "名字不能為空白！";
      } else if (this.Account == "") {
        this.Alarm_text = "帳號不能為空白！";
      } else if (this.Password == "") {
        this.Alarm_text = "密碼不能為空白！";
      } else if (this.Password_twice != this.Password) {
        this.Alarm_text = "密碼不一致！";
      } else {
        //this.Is_alarm = false;
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            id: this.Account,
            name: this.Name,
            password: this.Password,
          }),
        };
        const response = await fetch("/users/register", requestOptions);
        const res = await response.json();
        if (res.message == "success") {
          this.Alarm_text = "註冊成功";
          await new Promise((r) => setTimeout(r, 1000));
          var i = res.data.id;
          var n = res.data.name;
          this.$store.commit("setUserInformation", { i, n });
          this.$store.commit("setLogin", false);
          this.Alarm_text = "";
        } else {
          if (res.detail == "ID already registered") {
            this.Alarm_text = "帳號已存在！";
          } else {
            this.Alarm_text = res.detail;
          }
        }
      }
    },
    async Commit_signin() {
      this.Is_alarm = true;
      if (this.Account == "") {
        this.Alarm_text = "帳號不能為空白！";
      } else if (this.Password == "") {
        this.Alarm_text = "密碼不能為空白！";
      } else {
        //this.Is_alarm = false;
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            id: this.Account,
            password: this.Password,
          }),
        };
        const response = await fetch("/users/login", requestOptions);
        const res = await response.json();
        if (res.message == "success") {
          this.Alarm_text = "登入成功";
          await new Promise((r) => setTimeout(r, 1000));
          var i = res.data.id;
          var n = res.data.name;
          this.$store.commit("setUserInformation", { i, n });
          this.$store.commit("setLogin", false);
          this.Alarm_text = "";
        } else {
          if (res.detail == "Invalid ID/Password") {
            this.Alarm_text = "帳號或密碼輸入錯誤！";
          } else {
            this.Alarm_text = res.detail;
          }
        }
      }
    },
    Detect_enter(e) {
      if (e.key == "Enter") {
        this.Commit();
      }
    },
  },
  created() {
    window.addEventListener("keydown", this.Detect_enter);
  },
  unmounted() {
    window.removeEventListener("keydown", this.Detect_enter);
  },
  computed: {
    Alarm_text_color: function () {
      var r;
      if (this.Alarm_text == "登入成功" || this.Alarm_text == "註冊成功") {
        r = "green";
      } else {
        r = "red";
      }
      return r;
    },
  },
  components: {
    //HelloWorld
    PopupFrame,
  },
};
</script>

<style scoped>
.sign-up-pop .sign-up-header {
  display: flex;
  text-align: left;
  align-items: center;
  padding: 1rem;
  border-bottom-style: solid;
  border-bottom-width: 3px;
  border-bottom-color: #c4c4c4;
  height: 10%;
}

.sign-up-pop .sign-up-content {
  padding: 1rem;
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 70%;
}

.sign-up-pop .sign-up-content table {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  width: 30rem;
}

.sign-up-pop .sign-up-content input[type="text"],
.sign-up-pop .sign-up-content input[type="password"] {
  width: 20rem;
}

.sign-up-pop .sign-up-content table td {
  padding: 0.5rem 0 0.5rem 0;
}

.sign-up-pop .button-group {
  display: flex;
  justify-content: flex-end;
  height: 20%;
  padding: 1rem;
}

.sign-up-pop .button-group input[type="button"],
.sign-up-pop .button-group input[type="submit"] {
  margin: auto 0.5rem auto 0.5rem;
  font-family: inherit;
  font-size: inherit;
  width: 6rem;
  height: 2rem;
  border-radius: 5px;
  box-shadow: none;
  border-style: solid;
}

.sign-up-pop .button-group input[type="button"]:hover {
  background-color: rgb(206, 206, 206);
}

.sign-up-pop .button-group input[type="submit"]:hover {
  background-color: #1a82c7;
}

.sign-up-pop .button-group input[type="button"]:active {
  background-color: rgb(158, 158, 158);
}

.sign-up-pop .button-group input[type="submit"]:active {
  background-color: #16679c;
}

.sign-up-pop .button-group input[type="button"] {
  background-color: white;
}

.sign-up-pop .button-group input[type="submit"] {
  background-color: #18a0fb;
  color: white;
}
</style>
