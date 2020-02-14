import React from 'react';
import './App.css';
import { Route } from 'react-router-dom';

// Importing components
import Blockchain_Container from './components/chain/Blockchain_Container';

function App() {
  return (
    <div className="App">
      <Route path='/' component={Blockchain_Container} />
    </div>
  );
}

export default App;
