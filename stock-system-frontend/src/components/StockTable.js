// src/StockTable.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const StockTable = () => {
  const [stocks, setStocks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStocks = async () => {
      try {
        // Replace with your actual API endpoint
        const response = await axios.get('https://api.example.com/stocks');
        setStocks(response.data.data);
      } catch (err) {
        setError('Failed to fetch stocks');
      } finally {
        setLoading(false);
      }
    };

    fetchStocks();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h1>Stock Portfolio</h1>
      <table>
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Quantity</th>
            <th>Average Price</th>
            <th>Current Price</th>
            <th>Appreciation</th>
            <th>Rating</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map(stock => (
            <tr key={stock.id}>
              <td dangerouslySetInnerHTML={{ __html: stock.ticker }}></td>
              <td>{stock.quantity}</td>
              <td>{stock.avg_price.toFixed(2)}</td>
              <td>{stock.current_price.toFixed(2)}</td>
              <td>{stock.appreciation.toFixed(2)}%</td>
              <td dangerouslySetInnerHTML={{ __html: stock.avg_rating }}></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StockTable;