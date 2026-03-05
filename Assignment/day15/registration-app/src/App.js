import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Register from "./components/Register";
import Welcome from "./components/Welcome";
import Navbar from "./components/Navbar";

function App() {
  const [user, setUser] = useState("");

  return (
    <BrowserRouter>
      <Navbar user={user} setUser={setUser} />
      <Routes>
        <Route path="/" element={<Register setUser={setUser} />} />
        <Route path="/welcome" element={<Welcome user={user} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
