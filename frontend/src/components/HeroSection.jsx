
import React from 'react';
import doctorsImg from '../assets/doctors.png';


const HeroSection = () => {
  return (
    <section className="hero">
      <div>
        <h1>Your Health is Our <span style={{ color: '#007bff' }}>Priority</span></h1>
        <p>Book appointments, consult doctors, and manage your health all in one platform.</p>
        <button className="btn btn-primary">Book an Appointment</button>
      </div>
      <img src={doctorsImg} alt="Doctors" />
    </section>
  );
};

export default HeroSection;
