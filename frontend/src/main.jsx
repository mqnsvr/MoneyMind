import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import {AuthProvider} from './context/AuthContext.jsx'
import {WalletProvider} from './context/WalletContext.jsx'



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter> 
      <AuthProvider>
        <WalletProvider>
          <App />
        </WalletProvider>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
