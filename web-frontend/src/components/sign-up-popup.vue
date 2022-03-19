<template>
  <popup-frame>
    <div class="sign-up-header">
      <span>註冊帳號</span>
    </div>

    <div class="sign-up-content">
      <table>
        <tr>
          <td width="25%">
            <label for="account">帳號</label>
          </td>
          <td>
            <input type="text" id="account" />
          </td>
        </tr>
        <tr>
          <td>
            <label for="password">密碼</label>
          </td>
          <td>
            <input type="password" id="password" />
          </td>
        </tr>
        <tr>
          <td>
            <label for="password-twice">確認密碼</label>
          </td>
          <td>
            <input type="password" id="password-twice" />
          </td>
        </tr>
      </table>
    </div>
    <div class="button-group">
      <input type="button" value="取消" />
      <input type="submit" value="註冊" />
    </div>
  </popup-frame>
</template>

<script>
import PopupFrame from "./PopupFrame.vue";
export default {
  name: "sign-up-popup",
  components: {
    //HelloWorld
    PopupFrame,
  },
};
</script>

<style scoped>
.sign-up-pop {
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: column;
  position: absolute;
  left: 23.26%;
  right: 23.26%;
  top: 25.68%;
  bottom: 25.68%;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  border-style: solid;
  border-width: 1px;
  border-color: #c4c4c4;
  font-family: "微軟正黑體";
}

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
