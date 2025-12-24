import { NavLink } from "react-router-dom";
import { LayoutDashboard, Wallet, Receipt, PiggyBank, Sparkles, LogOut } from "lucide-react";
import { useAuth } from "../../context/AuthContext";

const items = [
  { to: "/app/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { to: "/app/expenses", label: "Expenses", icon: Receipt },
  { to: "/app/budgets", label: "Budgets", icon: PiggyBank },
  { to: "/app/wallets", label: "Wallets", icon: Wallet },
  { to: "/app/insights", label: "AI Insights", icon: Sparkles },
];

export default function Sidebar() {
  const { user, logout } = useAuth();

  return (
    <aside className="sidebar">
      <div className="sidebar-brand-row">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="currentColor"
          className="sidebar-logo"
          width="40"
          height="40"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M21 12a2.25 2.25 0 0 0-2.25-2.25H15a3 3 0 1 1-6 0H5.25A2.25 2.25 0 0 0 3 12m18 0v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6m18 0V9M3 12V9m18 0a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 9m18 0V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v3"
          />
        </svg>

        <div className="sidebar-brand">MoneyMind</div>
      </div>

      <nav className="sidebar-nav">
        {items.map(({ to, label, icon: Icon }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) => (isActive ? "sidebar-link active" : "sidebar-link")}
          >
            <Icon className="sidebar-icon" size={18} />
            {label}
          </NavLink>
        ))}
      </nav>

      <div className="sidebar-user">
        <div className="sidebar-user-row">
          <div className="sidebar-email">{user?.email}</div>
          <button onClick={logout} className="sidebar-logout-icon" aria-label="Logout">
            <LogOut size={16} />
          </button>
        </div>
      </div>
    </aside>
  );
}
