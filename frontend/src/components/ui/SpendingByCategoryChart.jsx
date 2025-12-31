import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function SpendingByCategoryChart({ data }) {
    return (
        <div style={{ height: 280 }}>
            
            <ResponsiveContainer width="100%" height="100%">
                <BarChart data={data}>
                    <XAxis dataKey="category" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="amount" fill="#0ea5a4" />
                </BarChart>
            </ResponsiveContainer>
        </div>
    );
}