export default function Card({ title, children }) {
  return (
    <div className="bg-white/70 backdrop-blur-md p-5 rounded-xl shadow-xl border">
      <h2 className="text-lg font-semibold mb-3 text-blue-700">{title}</h2>
      {children}
    </div>
  );
}
