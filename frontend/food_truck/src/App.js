import "./App.css";
import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";

import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

const customIcon = new Icon({
  iconUrl: "/food-truck.png",
  iconSize: [32, 32], // Adjust icon size as needed
});

function App() {
  const [foodTrucks, setFoodTrucks] = useState([]);
  const [cuisineFilter, setCuisineFilter] = useState(""); 

  useEffect(() => {
    fetchData();
  }, [cuisineFilter]); // Fetch data whenever cuisineFilter changes

  const fetchData = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/food-trucks/?cuisine=${cuisineFilter}`
      );
      const data = await response.json();
      setFoodTrucks(data); // Update state with food truck data
    } catch (error) {
      console.error("Error fetching food trucks:", error);
    }
  };

  const handleInputChange = (event) => {
    setCuisineFilter(event.target.value);
  };

  return (
    <div className="main">
      <navbar className="nav-bar">
        <img className="logo" src="/logo-color.png" alt="logo" />
        <input
          className="search-bar"
          type="text"
          placeholder="Enter Cuisine"
          value={cuisineFilter}
          onChange={handleInputChange}
        />
        <h2 className="title">Elias - Take Home Challenge</h2>
      </navbar>

      <MapContainer
        center={[37.747772091607466, -122.39703171897757]}
        zoom={15}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

        {foodTrucks.map((truck) => (
          <Marker
            key={truck.id}
            position={[truck.latitude, truck.longitude]}
            icon={customIcon}
          >
            <Popup>
              <div>
                <h3>{truck.name}</h3>
                <p>Applicant: {truck.applicant}</p>
                <p>Facility Type: {truck.facility_type}</p>
                <p>Adress: {truck.address}</p>
                <p>Location: {truck.location_description}</p>
                <p>Food Items: {truck.food_items}</p>
                <p>
                  Schedule:{" "}
                  <a href={truck.schedule} target="_blank" rel="noreferrer">
                    Click here
                  </a>
                </p>
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
