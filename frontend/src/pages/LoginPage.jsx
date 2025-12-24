import {useState} from "react";
import {useAuth} from "../context/AuthContext.jsx";
import {useNavigate, Link, replace} from "react-router-dom";

const API_BASE_URL = "http://localhost:8000/api/v1";

function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);
    const {login} = useAuth();
    const navigate = useNavigate();

    async function handleSubmit(event) {
        event.preventDefault(); // verhindert kompletten Seiten-Reload
        setError(null);

        try {
            // 1. Login-Request: /auth/login (Form-Daten, nicht JSON)
            const formData = new URLSearchParams();
            formData.append("username", email);
            formData.append("password", password);

            const response = await fetch(`${API_BASE_URL}/auth/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: formData.toString(),
            });

            const data = await response.json().catch(() => null);

            if (!response.ok) {
                throw new Error(data?.detail || "Login failed");
            }
            

            const accessToken = data.access_token;

            // 2. User-Daten holen: /auth/me (mit Token)
            const meResponse = await fetch(`${API_BASE_URL}/auth/me`, {
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                },
            });

            const userData = await meResponse.json().catch(() => null);

            if (!meResponse.ok) {
                throw new Error("Failed to fetch user data");
            }

            

            // 3. Im AuthContext speichern
            login(accessToken, userData);

            // 4. Zur Dashboard-Seite weiterleiten
            navigate("/app/dashboard", { replace: true }); 
        } catch (err) {
            setError(err.message);
        }
    }

    return (
        <div className="auth-page">
            <div className="auth-card">
                <h1 className="auth-title">
                    Willkommen zurück
                </h1>
                <p className="auth-subtitle">Melde dich mit deiner Email und deinem Passwort an, um deine Wallets zu verwalten.</p>

                {error && <p className="auth-error">{error}</p>}


                <form className="auth-form" onSubmit={handleSubmit}>
                    <div className="auth-field">
                        <label className="auth-label">E-Mail</label>
                        <input 
                        className="auth-input" 
                        type="text"
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

                    <button className="btn-primary" type="submit" style={{ marginTop: '0.5rem', width: '100%'}}>
                        Einloggen
                    </button>
                </form>

                <div className="auth-footer">
                    Noch kein Konto?{" "}
                    <Link to="/register" className="auth-link">
                    Jetzt Registrieren
                    </Link>
                </div>
            </div>
        </div>
    );
}


export default LoginPage;