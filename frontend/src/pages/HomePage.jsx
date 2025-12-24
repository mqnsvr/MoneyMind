import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function HomePage() {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();

  function handlePrimaryClick() {
    if (isAuthenticated) {
      navigate("/dashboard");
    } else {
      navigate("/register");
    }
  }

  function handleSecondaryClick() {
    if (isAuthenticated) {
      navigate("/dashboard");
    } else {
      navigate("/login");
    }
  }

  return (
    <div className="hero">
      {/* Linke Seite: Text + Buttons */}
      <div>
        <h1 className="hero-title">
          Behalte gemeinsame Finanzen im Blick –
          <br />
          ohne Excel-Chaos.
        </h1>
        <p className="hero-subtitle">
          MoneyMind hilft dir, geteilte Wallets mit Freunden, Partnern oder WG-Mitbewohnern
          zu organisieren: Ausgaben tracken, Budgets setzen, fair teilen.
        </p>
        <div className="hero-actions">
          <button className="btn-primary" onClick={handlePrimaryClick}>
            {isAuthenticated ? "Zum Dashboard" : "Kostenlos starten"}
          </button>
          <button className="btn-secondary" onClick={handleSecondaryClick}>
            {isAuthenticated ? "Wallets ansehen" : "Einloggen"}
          </button>
        </div>
      </div>

      {/* Rechte Seite: Demo-Karte */}
      <div className="hero-card">
        <h2 style={{ fontSize: "1rem", marginBottom: "0.75rem" }}>
          Beispiel-Wallet: „WG-Konto“
        </h2>
        <p style={{ fontSize: "0.85rem", color: "#9ca3af", marginBottom: "1rem" }}>
          Letzte Ausgaben
        </p>
        <ul style={{ listStyle: "none", fontSize: "0.9rem", marginBottom: "1rem" }}>
          <li style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.4rem" }}>
            <span>Einkauf Rewe</span>
            <span>- 37,80 €</span>
          </li>
          <li style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.4rem" }}>
            <span>Internet</span>
            <span>- 29,99 €</span>
          </li>
          <li style={{ display: "flex", justifyContent: "space-between" }}>
            <span>Miete</span>
            <span>- 550,00 €</span>
          </li>
        </ul>
        <div style={{ fontSize: "0.85rem", color: "#9ca3af" }}>
          <span>Budget Monat: 800 €</span>
          <br />
          <span>Verbraucht: 617,79 €</span>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
