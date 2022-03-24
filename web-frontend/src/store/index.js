import { createStore } from "vuex";

export default createStore({
  state: {
    ID: "",
    password: "",
    isLogin: false,
    isRegister: false,
  },
  getters: {},
  mutations: {
    setLogin(state, isLogin) {
      state.isLogin = isLogin;
    },
    setRegister(state, isRegister) {
      state.isRegister = isRegister;
    },
  },
  actions: {},
  modules: {},
});
