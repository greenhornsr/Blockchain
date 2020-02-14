import React from 'react';
import './App.css';
import { Route } from 'react-router-dom';

// Importing components
import Home from './components/Home';
import Blockchain_Container from './components/chain/Blockchain_Container';

function App() {
  return (
    <div className="App">
      <Route exact path="/" component={Home} />
      <Route path='/chain' component={Blockchain_Container} />
    </div>
  );
}

export default App;
