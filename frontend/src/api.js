import axios from "axios";

export const api = axios.create({
  baseURL: "https://backendserverv1.up.railway.app",
});
