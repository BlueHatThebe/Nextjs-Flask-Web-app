// components/DataList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataList = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/data');
      console.log('Data from Flask API:', response.data);
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h2>Data List</h2>
      <ul>
        {data.map((item, index) => (
          <li key={index}>
            ID: {item.id}, Name: {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DataList;


