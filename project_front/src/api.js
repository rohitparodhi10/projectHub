import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const apiURL="/choreo-apis/projecthub/backend/v1"

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiURL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => response, 
  (error) => {
    if (error.response?.status === 401) {
     
      localStorage.removeItem(ACCESS_TOKEN); 
      window.location.href = "/login"; 
    }
    return Promise.reject(error); 
  }
);


export default api;
