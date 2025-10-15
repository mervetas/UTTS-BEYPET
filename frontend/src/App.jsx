import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import Dashboard from "./Dashboard";
import MontajIslemleri from './MontajIslemleri';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/dashboard/montaj_islemleri" element={<MontajIslemleri />} />
      </Routes>
    </Router>
  );
}

export default App;
