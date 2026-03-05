
import React from "react";
import { useLocation } from "react-router-dom";

function Welcome({ user }) {
  const location = useLocation();
  const data = location.state;

  return (
    <div>
      <h2>Welcome Page</h2>
      <p>Name: {data.name}</p>
      <p>Email: {data.email}</p>
      <p>Phone: {data.phone}</p>
      <p>Address: {data.address}</p>
    </div>
  );
}

export default Welcome;


