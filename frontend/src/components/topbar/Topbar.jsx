import WalletSwitcher from "./WalletSwitcher";

export default function Topbar() {
    return (
        <div style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            padding: "16px 24px",
            backgroundColor: "#f5f5f5",
            borderBottom: "1px solid #ddd"
        }}>
            <div style={{display: "flex", alignItems: "center", gap: "12px"}}>
              <WalletSwitcher />
            </div>

            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <input placeholder="Search..."
                style={{
                  width: 260, padding: "10px 12px", borderRadius: 10, border: "1px solid #ccc"
                }}
              />
              <button style={{
                padding: "10px 12px", borderRadius: 10, border: "none", backgroundColor: "#007bff", color: "#fff", cursor: "pointer", background: "#0ea5a4", fontWeight: 600
              }}>
                + New Expense
              </button>
            </div>
        </div>
    );
}