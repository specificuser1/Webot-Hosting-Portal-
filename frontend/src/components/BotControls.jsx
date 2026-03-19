import { api } from "../api";
import Card from "./Card";

export default function BotControls() {
  const start = async () => {
    await api.post("/bots/start");
    alert("Bots Started");
  };

  const stop = async () => {
    await api.post("/bots/stop");
    alert("Bots Stopped");
  };

  return (
    <Card title="Bot Controls">
      <div className="flex gap-3">
        <button
          onClick={start}
          className="px-5 py-2 bg-green-600 text-white rounded-lg"
        >
          Start All
        </button>

        <button
          onClick={stop}
          className="px-5 py-2 bg-red-600 text-white rounded-lg"
        >
          Stop All
        </button>
      </div>
    </Card>
  );
}
