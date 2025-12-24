import {Outlet} from "react-router-dom";
import Sidebar from "../components/sidebar/Sidebar.jsx";
import Topbar from "../components/topbar/Topbar.jsx";

export default function AppShell() {
  return (
    <div style={{ display:"flex", minHeight: "100vh" }}>

        <Sidebar />
        <div style={{ flex: 1, background: "#f6f7fb" }}>
            <Topbar />
            <div style={{padding: "24px"}}>
                <Outlet />
            </div>
        </div>

    </div>
    );  
}