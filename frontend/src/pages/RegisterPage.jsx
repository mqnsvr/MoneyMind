import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api } from "../api/client";

function RegisterPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);

    try {
      await api.post("/auth/register", {
        body: { email, password },
      });

      navigate("/login");
    } catch (err) {
      setError(err.data?.detail || err.message);
    }
  }

  return (
    <div className="auth-page">
      <div className="auth-card">
        <h1 className="auth-title">Konto erstellen</h1>
        <p className="auth-subtitle">
          Erstelle ein kostenloses MoneyMind-Konto und tracke gemeinsame Finanzen mit Freunden oder WG.
        </p>

        {error && <p className="auth-error">{error}</p>}

        <form className="auth-form" onSubmit={handleSubmit}>
          <div className="auth-field">
            <label className="auth-label">E-Mail</label>
            <input
              className="auth-input"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              placeholder="du@example.com"
            />
          </div>

          <div className="auth-field">
            <label className="auth-label">Passwort</label>
            <input
              className="auth-input"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="Mindestens 8 Zeichen"
            />
          </div>

          <button type="submit" className="btn-primary" style={{ width: "100%", marginTop: "0.5rem" }}>
            Konto erstellen
          </button>
        </form>

        <div className="auth-footer">
          Schon ein Konto?{" "}
          <Link to="/login" className="auth-link">
            Zum Login
          </Link>
        </div>
      </div>
    </div>
  );
}

export default RegisterPage;
