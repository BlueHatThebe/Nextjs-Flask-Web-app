import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataList = () => {
  const [data, setData] = useState(null); // Initialize state as null

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/data');
      console.log('Data from Flask API:', response.data);

      setData(response.data); // Set data directly
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  console.log('Current data state:', data); // Log current data state

  return (
    <div>
      <h2>Data Details</h2>
      {data ? (
        <div>
          <p>ID: {data.id}</p>
          <p>Name: {data.name}</p>
          <p>Owner: {data.owner}</p>
          <p>Date Created: {data.date_created}</p>
          <p>Date Modified: {data.date_modified}</p>
          <p>Domain: {data.domain}</p>
          <p>Visibility: {data.visibility}</p>
          <p>Actuators: {data.actuators.length > 0 ? data.actuators.map(actuator => actuator.name).join(', ') : 'None'}</p>
          <p>Sensors:</p>
          <ul>
            {data.sensors.length > 0 ? (
              data.sensors.map((sensor, index) => (
                <li key={index}>
                  ID: {sensor.id}, Name: {sensor.name}, Quantity Kind: {sensor.quantity_kind}
                  {sensor.value ? (
                    <ul>
                      <li>
                        Value: {sensor.value.value} {sensor.unit}
                      </li>
                      <li>
                        Timestamp: {sensor.value.timestamp}
                      </li>
                    </ul>
                  ) : (
                    <p>No values available</p>
                  )}
                </li>
              ))
            ) : (
              <li>No sensors available</li>
            )}
          </ul>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default DataList;
