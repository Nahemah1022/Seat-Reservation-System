import axios from "axios";
import qs from "qs";

const service = axios.create({
  baseURL: "http://140.116.249.231:8000/",
  withCredentials: true,
  timeout: 5000,
  headers: {
    "Access-Control-Allow-Origin": "*",
    "content-type": "application/json",
    server: "uvicorn",
  },
});

service.interceptors.request.use(
  (config) => {
    if (!config.data) {
      config.data = {};
    }
    console.log(qs.stringify(config.data));
    return config;
  },
  (error) => {
    console.log(error);
    return Promise.reject(error);
  }
);
service.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.log(error);
    return Promise.reject(error);
  }
);

export default service;
