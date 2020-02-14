import React from 'react';
import './App.css';
import { Route } from 'react-router-dom';

// Importing components
import Home from './components/Home';
import Blockchain_Container from './components/chain/Blockchain_Container';
import LastBlock_Container from './components/lastblock/LastBlock_Container';

function App() {
  return (
    <div className="App">
      <Route exact path="/" component={Home} />
      <Route path='/chain' component={Blockchain_Container} />
      <Route path='/last_block' component={LastBlock_Container} />
    </div>
  );
}

export default App;
