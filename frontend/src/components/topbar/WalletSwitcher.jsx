import {useEffect, useState} from 'react';
import {useWallet} from '../../context/WalletContext.jsx';
import {useAuth} from '../../context/AuthContext.jsx';
import {api} from '../../api/client.js';


export default function WalletSwitcher() {
    const {token} = useAuth();
    const {activeWalletId, setActiveWalletId} = useWallet();
    const [wallets, setWallets] = useState([]);

    useEffect(() => {
        async function load() {
            const data = await api.get("/wallets", {token});
            setWallets(data);
            if (!activeWalletId && data.length > 0) setActiveWalletId(data[0].id);
        }
        load().catch(console.error);
    }, [token]);

    return (
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{fontWeight: 700}}>Active Wallet:</span>
            <select
            value={activeWalletId ?? ""}
            onChange={(e) => setActiveWalletId(Number(e.target.value))}
            style={{ padding: "4px", borderRadius: "4px", border: "1px solid #ccc" }}
        >
            {wallets.map((w) => (
                <option key={w.id} value={w.id}>
                    {w.name}
                </option>
            ))}

            </select>
        </div>
    );
}