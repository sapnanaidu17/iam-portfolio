import React, { useState } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [token, setToken] = useState("");

  const login = async () => {
    const res = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username })
    });
    const data = await res.json();
    setToken(data.access_token);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>SSO Demo Login</h1>
      <input 
        type="text"
        placeholder="Username" 
        onChange={(e) => setUsername(e.target.value)} 
      />
      <button onClick={login}>Login</button>
      {token && (
        <div>
          <h3>JWT Token:</h3>
          <p style={{ wordBreak: "break-all" }}>{token}</p>
        </div>
      )}
    </div>
  );
}

export default App;
