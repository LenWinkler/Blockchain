import React, { useEffect, useState } from 'react';
import './App.css';

import axios from 'axios';

function App() {

  const [chain, setChain] = useState([]);
  const [transactions, setTransactions] = useState();

  useEffect(() => {
    axios.get('http://localhost:5000/chain')
    .then(res => {
      console.log('res', res.data.chain)
      setChain(res.data.chain)
      console.log('chain', chain)
    })
    .catch(err => console.log('GET error',err))
  }, [])

  return (
    <div className="App">
      <p>Wallet app</p>
    </div>
  );
}

export default App;
