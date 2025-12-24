import {Link} from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function NavBar() {
  const { isAuthenticated, user, logout } = useAuth();

  return (
    <header className="navbar">
        <div className="navbar-brand" style={{ display: 'flex', alignItems: 'center', gap: '0.8rem'}}>
            <div className="navbar-logo">
            <svg 
            xmlns="http://www.w3.org/2000/svg"
            fill="none" viewBox="0 0 24 24" 
            strokeWidth={1.5} 
            stroke="currentColor" 
            className="size-6"
            width="40"
            height="40">
              <path strokeLinecap="round" strokeLinejoin="round" d="M21 12a2.25 2.25 0 0 0-2.25-2.25H15a3 3 0 1 1-6 0H5.25A2.25 2.25 0 0 0 3 12m18 0v6a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 18v-6m18 0V9M3 12V9m18 0a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 9m18 0V6a2.25 2.25 0 0 0-2.25-2.25H5.25A2.25 2.25 0 0 0 3 6v3" />
            </svg>
        </div>
            MoneyMind
        </div>
        <nav className="navbar-links">
            {!isAuthenticated && (
                <>
                    <Link to="/login" className="navbar-link">Login</Link>
                    <Link to="/register" className="navbar-link">Register</Link>
                </>
            )}
            {isAuthenticated && (
                <>
                    <span className="navbar-link">Hallo, {user?.username}</span>
                    <Link to="/dashboard" className="navbar-link">
                    Dashboard
                    </Link>
                    <button 
                      type="button" 
                      className="navbar-link"
                      style={{ background: 'none', border: 'none', padding: 0, cursor: 'pointer', font: 'inherit', color: 'inherit' }}
                      onClick={logout}>

                    </button>
                </>
            )}
        </nav>
    </header>
  );
}

export default NavBar;
