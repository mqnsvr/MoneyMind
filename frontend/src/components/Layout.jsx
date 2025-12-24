import NavBar from "./NavBar"

function Layout({ children }) {
  return (
    <div className="app-shell">
      <NavBar />
      <main className="app-content">
        {children}
      </main>
    </div>
  );
}

export default Layout;
