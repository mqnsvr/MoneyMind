import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { api } from "../api/client";
import StatCard from "../components/ui/StatCard";
import SpendingByCategoryChart from "../components/ui/SpendingByCategoryChart";


function DashboardPage() {
  const { token, logout } = useAuth();
  const [wallets, setWallets] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  // Mock (später durch useDashboardData ersetzen)
  const stats = {
    totalSpent: "€615.50",
    budgetsActive: "3",
    members: "5",
  };

  const chartData = [
    { category: "Transport", amount: 155.5 },
    { category: "Food", amount: 210.0 },
    { category: "Rent", amount: 250.0 },
  ];


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
    <div className="dashboard">
      <h1 className="dashboard-title">Dashboard</h1>

      <div className="stats-grid">
        <StatCard title="TOTAL SPENT THIS MONTH" value={stats.totalSpent} subtitle="↑ vs last month" />
        <StatCard title="ACTIVE BUDGETS" value={stats.budgetsActive} subtitle="Tracking across categories" />
        <StatCard title="SHARED MEMBERS" value={stats.members} subtitle="Members in wallet" />
      </div>

      <div className="main-grid">
        <div className="card">
          <div className="card-title">Spending by Category</div>
          <SpendingByCategoryChart data={chartData} />
        </div>

        <div className="card">
          <div className="card-title">Budget Health</div>
          {/* hier später echte Budget-Fortschritte */}
          <div className="budget-section">
            <div className="progress-row">
              <span>Transport</span><span>€15.50 / €100.00</span>
            </div>
            <div className="progress-bar-container">
              <div className="progress-bar" style={{ width: "15%" }} />
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="card-title">Recent Transactions</div>
        {/* als nächstes: Table-Komponente */}
        <div className="recent-placeholder">… Tabelle kommt als nächster Baustein</div>
      </div>
    </div>
  );
}

export default DashboardPage;
