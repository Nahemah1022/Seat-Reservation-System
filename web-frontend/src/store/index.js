import { createStore } from "vuex";

export default createStore({
  state: {
    ID: "",
    password: "",
    name: "",
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
    setUserInformation(state, item) {
      state.ID = item.i;
      state.name = item.n;
    },
  },
  actions: {},
  modules: {},
});
