import React, { createContext, useState, useContext, useEffect } from "react";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
    // beim Laden: Token & User als localStorage wiederherstellen
  const [token, setToken] = useState(() => localStorage.getItem("token"));
  const [user, setUser] = useState(() => {
    const stored = localStorage.getItem("user");
    return stored ? JSON.parse(stored) : null;
  });


useEffect(() => {
    // Token im localStorage speichern/entfernen
  if (token) {
    localStorage.setItem("token", token);
  } else {
    localStorage.removeItem("token");
  }
}, [token]);

useEffect(() => {
    // User im localStorage speichern/entfernen
  if (user) {
    localStorage.setItem("user", JSON.stringify(user));
  } else {
    localStorage.removeItem("user");
  }
  }, [user]);

  function login(newToken, userData){
    setToken(newToken);
    setUser(userData);
  }

  function logout(){
    setToken(null);
    setUser(null);
  }

  const value = { token, user, login, logout };
  
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}   

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return ctx;
}