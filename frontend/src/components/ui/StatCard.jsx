export default function StatCard({ title, value, subtitle }) {
    return (
        <div style={{
            backgroundColor: "#fff",
            borderRadius: 14,
            padding: 16,
            border: "1px solid #e6e8f0",
        }}>
            <div style={{fontSize: 12, opacity: 0.7, fontWeight: 700}}> {title}</div>
            <div style={{fontSize: 28, marginTop: 6, fontWeight: 800}}> {value}</div>
            {subtitle && (
                <div style={{fontSize: 12, opacity: 0.75, marginTop: 6}}> {subtitle}</div>
            )}

        </div>
    );
}