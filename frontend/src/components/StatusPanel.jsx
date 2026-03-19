import { useState } from "react";
import { api } from "../api";
import Card from "./Card";

export default function StatusPanel() {
  const [activity, setActivity] = useState("Playing");
  const [text, setText] = useState("");

  const apply = async () => {
    await api.post("/bots/status", { activity, text });
    alert("Status Updated");
  };

  return (
    <Card title="Custom Status & Activity">
      <select
        onChange={(e) => setActivity(e.target.value)}
        className="border p-2 rounded-lg w-full mb-3"
      >
        <option>Playing</option>
        <option>Watching</option>
        <option>Listening</option>
        <option>Streaming</option>
        <option>Competing</option>
      </select>

      <input
        type="text"
        placeholder="Custom status text"
        className="w-full p-2 border rounded-lg"
        onChange={(e) => setText(e.target.value)}
      />

      <button
        onClick={apply}
        className="mt-3 bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
      >
        Apply Status
      </button>
    </Card>
  );
}
