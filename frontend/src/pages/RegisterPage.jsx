import {useState} from "react";
import {api} from "../api/client.js";
import {useNavigate} from "react-router-dom";

function RegisterPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const [error, setError] = useState(null);

    async function handleSubmit(event) {
        event.preventDefault(); // verhindert kompletten Seiten-Reload
        setError(null);

        try{
            await api.post("/auth/register", {
                body: {
                    email: email,
                    password: password,
                },
            });

            // Nach erfolgreicher Registrierung zur Login-Seite weiterleiten
            navigate("/login");
        } catch (err) {
            setError(err.data?.detail || err.message);
        }
    }

    return (
        <div>
            <h1>Registrieren</h1>
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
                <button type="submit">Konto erstellen</button>  
            </form>
        </div>
    );
}

export default RegisterPage;
        