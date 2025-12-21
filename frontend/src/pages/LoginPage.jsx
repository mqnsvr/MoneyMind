import {useState} from "react";
import {useAuth} from "../context/AuthContext.jsx";
import {useNavigate} from "react-router-dom";

const API_BASE_URL = "http://localhost:8000/api/v1";

function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const {login} = useAuth();
    const navigate = useNavigate();
    const [error, setError] = useState(null);

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

            if (!response.ok) {
                const data = await response.json().catch(() =>null);
                throw new Error(data?.detail || "Login failed");
            }
            const tokenData = await response.json();

            const accessToken = tokenData.access_token;

            // 2. User-Daten holen: /auth/me (mit Token)
            const meResponse = await fetch(`${API_BASE_URL}/auth/me`, {
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                },
            });

            if (!meResponse.ok) {
                throw new Error("Failed to fetch user data");
            }

            const userData = await meResponse.json();

            // 3. Im AuthContext speichern
            login(accessToken, userData);

            // 4. Zur Dashboard-Seite weiterleiten
            navigate("/dashboard"); 
        } catch (err) {
            setError(err.message);
        }
    }

    return (
        <div>
            <h1>Login</h1>
            {error && <p style={{color: "red"}}>{error}</p>}

            <form onSubmit={handleSubmit}>
                <div>
                    <label>
                        E-Mail:
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </label>
                </div>
                <div>
                    <label>
                        Passwort:
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </label>
                </div>
                <button type="submit">Einloggen</button>
            </form>
        </div>
    );
}

export default LoginPage;