import Navbar from "./components/Navbar";
import AddBot from "./components/AddBot";
import BotControls from "./components/BotControls";
import StatusPanel from "./components/StatusPanel";
import LogsConsole from "./components/LogsConsole";

export default function App() {
  return (
    <div>
      <Navbar />

      <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <AddBot />
        <BotControls />
        <StatusPanel />
        <LogsConsole />
      </div>
    </div>
  );
}
