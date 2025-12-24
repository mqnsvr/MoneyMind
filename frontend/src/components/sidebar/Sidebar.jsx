import { NavLink } from "react-router-dom";
import {LayoutDashboard, Wallet, Receipt, PiggyBank, Sparkles} from "lucide-react";
import { useAuth } from "../../context/AuthContext";

const items = [
    { to: "/app/dashboard", label: "Dashboard", icon: <LayoutDashboard /> },
    { to: "/app/expenses", label: "Ausgaben", icon: <Receipt /> },
    { to: "/app/budgets", label: "Budgets", icon: <PiggyBank /> },
    { to: "/app/wallets", label: "Wallets", icon: <Wallet /> },
    { to: "/app/insights", label: "Insights", icon: <Sparkles /> },
];

export default function Sidebar() {
    return (
        <nav className="sidebar">
            {items.map((item) => (
                <NavLink key={item.to} to={item.to} className="sidebar-link">
                    {item.icon}
                    <span>{item.label}</span>
                </NavLink>
            ))}
        </nav>
    );
}

