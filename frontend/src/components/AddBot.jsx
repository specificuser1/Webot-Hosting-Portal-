import { useState } from "react";
import { api } from "../api";
import Card from "./Card";

export default function AddBot() {
  const [tokens, setTokens] = useState("");

  const addBulk = async () => {
    const list = tokens.split("\n").filter((x) => x.trim().length > 0);
    await api.post("/bot/add/bulk", { tokens: list });
    alert("Bots Added!");
  };

  return (
    <Card title="Add Bots (Single/Bulk)">
      <textarea
        className="w-full p-3 border rounded-lg"
        placeholder="Add 1 token per line"
        rows={5}
        onChange={(e) => setTokens(e.target.value)}
      ></textarea>

      <button
        onClick={addBulk}
        className="mt-3 bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
      >
        Upload Bots
      </button>
    </Card>
  );
}
