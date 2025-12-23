import {Navigate} from "react-router-dom";
import {useAuth} from "../context/AuthContext.jsx";

function PrivateRoute({ children }) {
    const { token } = useAuth();

    if (!token) {
        // wenn nicht eingeloggt: weiterleiten zur Login-Seite
        return <Navigate to="/login" replace />;
    }

    // wenn eingeloggt: geschützte Komponente rendern
    return children;
}

export default PrivateRoute;