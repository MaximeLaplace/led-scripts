import React, { useEffect, useState } from 'react';
import axios from 'axios';

import { Button, Grid } from '@mui/material';

import { TitleDivider } from './TitleDivider';

export const Modes = () => {
  const [modes, setModes] = useState<string[]>([]);

  useEffect(() => {
    const get = async () => {
      const { data } = await axios({
        url: '/start_mode',
        method: 'GET'
      });
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
    <>
      <TitleDivider title="Modes" />
      <Grid container spacing={4} justifyContent="center">
        {modes.length ? (
          modes.map((mode) => (
            <Grid key={mode} item xs={8} sm={3}>
              <Button variant="contained" fullWidth onClick={startMode(mode)}>
                {mode}
              </Button>
            </Grid>
          ))
        ) : (
          <Grid item>Loading modes...</Grid>
        )}
      </Grid>
    </>
  );
};
