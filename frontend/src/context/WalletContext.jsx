import {createContext, useContext, useState} from 'react';

const WalletContext = createContext(null);

export function WalletProvider({ children }) {
    const [activeWallet, setActiveWalletId] = useState([])
    
    return (
        <WalletContext.Provider value={{ activeWallet, setActiveWalletId }}>
            {children}
        </WalletContext.Provider>
    );
}

export function useWallet() {
    const ctx = useContext(WalletContext);
    if (!ctx) {
        throw new Error("useWallet must be used within a WalletProvider");
    }
    return ctx;
}