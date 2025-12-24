{/* App.jsx: Definiert die Routen der Anwendung
  Welche Seite bei welcher URL angezeigt wird. */}

import { Routes, Route, Navigate } from "react-router-dom";
import PublicLayout from "./layouts/PublicLayout";
import AppShell from "./layouts/AppShell";
import PrivateRoute from "./components/PrivateRoute";

import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";

import DashboardPage from "./pages/DashboardPage";
import ExpensesPage from "./pages/ExpensesPage";
import BudgetsPage from "./pages/BudgetsPage";
import WalletsPage from "./pages/WalletsPage";
import InsightsPage from "./pages/InsightsPage";

function App() {
  return (
      <Routes>
        {/* öffentliche Routen */}
        <Route element={<PublicLayout/>}>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
        </Route>
      

        {/* Private App Shell */}
        <Route
        path="/app"
        element={
          <PrivateRoute>
            <AppShell />
          </PrivateRoute>
        }
      >

        <Route index element={<Navigate to="app/dashboard" replace/>} />
        <Route path="dashboard" element={<DashboardPage />} />
        <Route path="expenses" element={<ExpensesPage />} />
        <Route path="budgets" element={<BudgetsPage />} />
        <Route path="wallets" element={<WalletsPage />} />
        <Route path="insights" element={<InsightsPage />} />


      </Route>
        
          

        

        <Route path="*" element={<Navigate to="/" replace/>} />
      </Routes>
  )
}

export default App;