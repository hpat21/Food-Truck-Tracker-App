import "./App.css";
import "leaflet/dist/leaflet.css";
import {Icon} from 'leaflet'

import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

const customIcon = new Icon({
  iconUrl: '/food-truck.png',
  iconSize: [32, 32], // Adjust icon size as needed
});

function App() {
  const [foodTrucks, setFoodTrucks] = useState([]);
  

  useEffect(() => {
    // Fetch food truck data from your API endpoint
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/food-trucks/");
        const data = await response.json();
        setFoodTrucks(data); // Update state with food truck data
      } catch (error) {
        console.error("Error fetching food trucks:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="main">
      <navbar className="nav-bar">
        <img className="logo" src="/logo-color.png" alt="logo" />
        
      </navbar>

      <MapContainer
        center={[37.747772091607466, -122.39703171897757]}
        zoom={15}
       
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
  
        {foodTrucks.map((truck) => (
          <Marker key={truck.id} position={[truck.latitude, truck.longitude]} icon={customIcon}>
            <Popup>
              <div>
                <h3>{truck.name}</h3>
                <p>Applicant: {truck.applicant}</p>
                <p>Facility Type: {truck.facility_type}</p>
                <p>Adress: {truck.address}</p>
                <p>Location: {truck.location_description}</p>
                <p>Food Items: {truck.food_items}</p>
                <p>Schedule: <a href={truck.schedule} target="_blank">Click here</a></p>
                <p>Status: {truck.status}</p>
              </div>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default App;
