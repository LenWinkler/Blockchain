import React, { useEffect, useState } from 'react';
import './App.css';

import axios from 'axios';

function App() {

  const [chain, setChain] = useState([]);
  const [transactions, setTransactions] = useState();
  const [user, setUser] = useState();
  const [sender, setSender] = useState();
  const [recipient, setRecipient] = useState();
  const [amount, setAmount] = useState();

  useEffect(() => {
    axios.get('http://localhost:5000/chain')
    .then(res => {
      setChain(res.data.chain)
    })
    .catch(err => console.log('GET error',err))
  },[])
 
  console.log(chain)

  return (
    <div className="App">
      <h1>Wallet</h1>


    </div>
  );
}

export default App;
