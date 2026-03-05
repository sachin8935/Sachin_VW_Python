import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register({ setUser }) {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setUser(form.name);
    navigate("/welcome", { state: form });
  };

  return (
    <div>
      <h2>Registration Form</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" onChange={handleChange} required />
        <br />
        <input name="email" placeholder="Email" onChange={handleChange} required />
        <br />
        <input name="phone" placeholder="Phone" onChange={handleChange} required />
        <br />
        <input name="address" placeholder="Address" onChange={handleChange} required />
        <br /><br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Register;
