import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const sendTravelQuery = async (question) => {
  const response = await api.post("/api/travel", {
    question,
  });

  return response.data;
};

export const getSearchHistory = async () => {
  const response = await api.get("/api/history");

  return response.data;
};

export const generateItinerary = async (
  destination,
  days,
  interests = "general sightseeing"
) => {
  const response = await api.post("/api/itinerary", {
    destination,
    days,
    interests,
  });

  return response.data;
};

export const askRAGQuestion = async (question) => {
  const response = await api.post("/api/rag/query", {
    question,
  });

  return response.data;
};

export const uploadTravelPDF = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post("/api/rag/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};