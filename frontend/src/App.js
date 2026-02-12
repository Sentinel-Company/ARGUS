import React, { useState } from 'react';
import ForceGraph3D from 'react-force-graph-3d';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:8000';

function App() {
  const [graphData, setGraphData] = useState({ nodes: [], links: [] });
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = async () => {
    const response = await axios.post(`${API_URL}/api/v1/search/person`, { query: searchQuery, limit: 20 });
    console.log(response.data);
  };

  const loadPersonGraph = async (personName) => {
    const response = await axios.get(`${API_URL}/api/v1/graph/person/${encodeURIComponent(personName)}`);
    const { nodes, edges } = response.data;
    setGraphData({
      nodes: nodes.map(n => ({ id: n.id, name: n.properties.name || `Node ${n.id}`, ...n.properties })),
      links: edges.map(e => ({ source: e.source, target: e.target, type: e.type }))
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>ARGUS: AI Relationship Graph</h1>
        <div className="search-bar">
          <input type="text" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} placeholder="Search..." />
          <button onClick={handleSearch}>Search</button>
        </div>
      </header>
      <div className="graph-container">
        <ForceGraph3D graphData={graphData} nodeLabel="name" nodeAutoColorBy="label" linkLabel="type" />
      </div>
    </div>
  );
}

export default App;
