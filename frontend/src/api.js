import axios from "axios";

export const api = axios.create({
  baseURL: "https://your-backend-service.up.railway.app",
});
