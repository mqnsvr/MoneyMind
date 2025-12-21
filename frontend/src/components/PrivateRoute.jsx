import {Navigate} from "react-router-dom";
import {useAuth} from "../context/AuthContext.jsx";

function PrivateRoute({ children }) {
    const {isAuthenticated} = useAuth();

    if (!isAuthenticated) {
        // wenn nicht eingeloggt: weiterleiten zur Login-Seite
        return <Navigate to="/login" replace />;
    }

    // wenn eingeloggt: geschützte Komponente rendern
    return children;
}

export default PrivateRoute;