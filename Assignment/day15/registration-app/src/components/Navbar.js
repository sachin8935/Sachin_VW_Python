
import React from "react";
import { useNavigate } from "react-router-dom";

function Navbar({ user, setUser }) {
  const navigate = useNavigate();

  const logout = () => {
    setUser("");
    navigate("/");
  };

  return (
    <div style={{ display: "flex", justifyContent: "flex-end", padding: "10px" }}>
      {user && (
        <>
          <span>Welcome {user}</span>
          <button onClick={logout} style={{ marginLeft: "10px" }}>
            Logout
          </button>
        </>
      )}
    </div>
  );
}

export default Navbar;
