import React, { useEffect, useState } from 'react';
import axios from 'axios';

import { Button, Grid } from '@mui/material';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';

import { AppBar } from './components/AppBar';

import './App.css';

const App: React.FC = () => {
  const [modes, setModes] = useState<string[]>([]);

  useEffect(() => {
    const get = async () => {
      const { data } = await axios({
        url: '/start_mode',
        method: 'GET'
      });
      console.log(data);
      setModes(data);
    };
    get();
  }, []);

  const startMode = (mode: string) => () => {
    axios({
      url: '/start_mode',
      method: 'POST',
      data: {
        mode
      }
    });
  };

  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar />
      <Box component="main" sx={{ p: 3 }}>
        <Toolbar />
        <Grid container spacing={4} justifyContent="center">
          {modes.length
            ? modes.map((mode) => (
                <Grid key={mode} item xs={8} sm={3}>
                  <Button
                    variant="contained"
                    fullWidth
                    onClick={startMode(mode)}
                  >
                    {mode}
                  </Button>
                </Grid>
              ))
            : 'Loading modes...'}
        </Grid>
      </Box>
    </Box>
  );
};

export { App };
