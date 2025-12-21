import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { api } from "../api/client";

function DashboardPage() {
  const { token } = useAuth();
  const [projects, setProjects] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadProjects() {
      try {
        // Beispiel: GET /projects — in deinem MoneyMind-Projekt wäre das z.B. /wallets
        const data = await api.get("/projects", { token });
        setProjects(data);
      } catch (err) {
        setError(err.message);
      }
    }

    loadProjects();
  }, [token]);

  return (
    <div>
      <h1>Dashboard</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul>
        {projects.map((p) => (
          <li key={p.id}>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default DashboardPage;
