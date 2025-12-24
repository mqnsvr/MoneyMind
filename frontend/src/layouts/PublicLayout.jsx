import NavBar from "../components/NavBar"
import { Outlet } from "react-router-dom";

function PublicLayout({ children }) {
  return (
    <div className="app-shell">
      <NavBar />
      <main className="app-content">
        <Outlet />
      </main>
    </div>
  );
}

export default PublicLayout;
