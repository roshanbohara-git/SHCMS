// src/Landing.jsx

import React, { useEffect } from 'react';
import '../styles/LandingPage.css'; // your custom styles
import logo from '../assets/logo.png'; 
import doctors from '../assets/doctors.png';

export default function Landing() {
  useEffect(() => {
    const menuToggle = document.getElementById('menuToggle');
    const navCenter = document.getElementById('navCenter');

    menuToggle.addEventListener('click', () => {
      navCenter.classList.toggle('active');
      const icon = menuToggle.querySelector('i');
      icon.classList.toggle('fa-bars');
      icon.classList.toggle('fa-times');
    });

    // Optional cleanup (not strictly needed here, but good habit)
    return () => {
      menuToggle.removeEventListener('click', () => {});
    };
  }, []);

  return (
    <>
      <header>
        <button className="menu-toggle" id="menuToggle">
          <i className="fas fa-bars"></i>
        </button>
        <div className="logo">
          <img src={logo} alt="OTC Care Logo" />
          OTC Care
        </div>
        <div className="nav-center" id="navCenter">
          <a href="#">Home</a>
          <a href="#">Services</a>
          <a href="#">Doctors</a>
          <a href="#">About</a>
          <a href="#">Contact</a>
        </div>
        <div className="auth-buttons">
          <button className="btn btn-outline">
            <i className="fas fa-sign-in-alt"></i> Login
          </button>
          <button className="btn btn-primary">
            <i className="fas fa-user-plus"></i> Sign Up
          </button>
        </div>
      </header>

      <section className="hero">
        <div className="hero-content">
          <h1>Your Health is Our Priority</h1>
          <p>
            Book appointments, consult doctors, and manage your health all in
            one place. Get personalized care from the comfort of your home.
          </p>
          <button className="btn btn-primary">
            <i className="fas fa-calendar-check"></i> Book Appointment
          </button>
        </div>
        <div className="hero-image">
          <img src={doctors} alt="Doctor consulting patient" />
        </div>
      </section>

      <footer>
        <div className="footer-content">
          <div className="footer-column">
            <h3>OTC Care</h3>
            <p>
              Your trusted healthcare partner providing quality medical services
              anytime, anywhere.
            </p>
            <div className="social-links">
              <a href="#"><i className="fab fa-facebook-f"></i></a>
              <a href="#"><i className="fab fa-twitter"></i></a>
              <a href="#"><i className="fab fa-instagram"></i></a>
              <a href="#"><i className="fab fa-linkedin-in"></i></a>
            </div>
          </div>
          <div className="footer-column">
            <h3>Quick Links</h3>
            <ul>
              <li><a href="#">Home</a></li>
              <li><a href="#">Services</a></li>
              <li><a href="#">Doctors</a></li>
              <li><a href="#">Appointments</a></li>
            </ul>
          </div>
          <div className="footer-column">
            <h3>Services</h3>
            <ul>
              <li><a href="#">Online Consultation</a></li>
              <li><a href="#">Health Checkups</a></li>
              <li><a href="#">Emergency Care</a></li>
              <li><a href="#">Medicine Delivery</a></li>
            </ul>
          </div>
          <div className="footer-column">
            <h3>Contact Us</h3>
            <ul>
              <li><i className="fas fa-map-marker-alt"></i> 123 Health St, Medical City</li>
              <li><i className="fas fa-phone"></i> +1 (555) 123-4567</li>
              <li><i className="fas fa-envelope"></i> info@otccare.com</li>
            </ul>
          </div>
        </div>
        <div className="copyright">
          <p>© 2023 OTC Care. All rights reserved.</p>
        </div>
      </footer>
    </>
  );
}
