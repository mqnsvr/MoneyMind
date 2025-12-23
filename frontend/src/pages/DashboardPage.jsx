import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { api } from "../api/client";

function DashboardPage() {
  const { token, logout } = useAuth();
  const [wallets, setWallets] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadWallets() {
      try {
        const data = await api.get("/wallets/", { token });
        setWallets(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    if (token) {
      loadWallets();
    }
  }, [token]);

  return (
    <div style={{ padding: "20px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>💰 MoneyMind Dashboard</h1>
        <button onClick={logout} style={{ padding: "8px 16px" }}>Abmelden</button>
      </div>
      
      {error && <p style={{ color: "red" }}>{error}</p>}
      {loading && <p>Lädt...</p>}

      <h2>Meine Wallets</h2>
      {!loading && wallets.length === 0 && <p>Keine Wallets vorhanden.</p>}
      
      <ul>
        {wallets.map((w) => (
          <li key={w.id}>{w.name} ({w.currency})</li>
        ))}
      </ul>
    </div>
  );
}

export default DashboardPage;
