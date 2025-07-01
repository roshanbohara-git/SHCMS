import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Landing from './pages/Landing.jsx';
import './App.css';
import DoctorLogin from './pages/doctor/DoctorLogin.jsx';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path = "/doctor/login" element={<DoctorLogin/>} />
        
      </Routes>
    </Router>
  );
};

export default App;
