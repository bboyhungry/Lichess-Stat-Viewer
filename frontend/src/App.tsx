import React from 'react';
import logo from './logo.svg';
import './App.css';
import SearchBar from './components/SearchBar';

function App() {
  return (
    <div className="App">
      <SearchBar username="testUser" />
    </div>
  );
}

export default App;
