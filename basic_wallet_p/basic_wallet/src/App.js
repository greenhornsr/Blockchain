import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Route } from 'react-router-dom';

// Importing components
import Blockchain_Container from './components/Blockchain_Container';

function App() {
  return (
    <div className="App">
      <Route path='/' component={Blockchain_Container} />
    </div>
  );
}

export default App;
