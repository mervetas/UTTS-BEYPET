import React from 'react';
import { Route, Routes } from 'react-router-dom';
import MontajIslemleri from './MontajIslemleri';
import Menu from './menu/menu'; // Import the updated menu component

const Dashboard = () => {
  return (
    <div style={{ display: 'flex' }}>
      {/* Left Sidebar Navigation*/}
      <Menu />

      {/* Main Content Area */}
      <div style={{ flex: 1, padding: '20px' }}>
        <Routes>
          <Route path="montaj_islemleri" element={<MontajIslemleri />} />
          {/* Add other application routes here as needed  */}
        </Routes>
      </div>
    </div>
  );
};

export default Dashboard;
