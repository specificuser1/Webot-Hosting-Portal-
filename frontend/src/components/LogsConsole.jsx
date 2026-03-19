import { useEffect, useState } from "react";
import Card from "./Card";

export default function LogsConsole() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("wss://your-backend-service.up.railway.app/ws/logs");

    ws.onmessage = (msg) =>
      setLogs((prev) => [...prev, msg.data]);

    return () => ws.close();
  }, []);

  return (
    <Card title="Live Console Logs">
      <div className="h-64 overflow-auto p-3 bg-black text-green-400 text-sm rounded-lg font-mono">
        {logs.map((line, i) => (
          <div key={i}>{line}</div>
        ))}
      </div>
    </Card>
  );
}
