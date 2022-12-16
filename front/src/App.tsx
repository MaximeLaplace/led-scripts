import React from 'react';

import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';

import { AppBar } from './components/AppBar';
import { Modes } from './components/Modes';
import { SegmentsToUse } from './components/SegmentsToUse';
import { SpeedFactor } from './components/SpeedFactor';

import './App.css';

const App: React.FC = () => {
  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar />
      <Box component="main" sx={{ p: 3 }}>
        <Toolbar />

        <SegmentsToUse />

        <SpeedFactor />

        <Modes />
      </Box>
    </Box>
  );
};

export { App };
