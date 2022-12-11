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
      console.log(data);
      setModes(data);
    };
    setModes([
      'bogo',
      'bouncing_pulse',
      'bubble_sort',
      'cellular_automaton',
      'christmas',
      'color_wipe',
      'demo',
      'french_cancan',
      'impact',
      'lamp',
      'pulse',
      'rainbow',
      'rainbowDemo',
      'segment_strobo',
      'slider_strobo',
      'strobo',
      'theater_chase',
      'theater_chase_rainbow'
    ]);
    // get();
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
        {modes.length
          ? modes.map((mode) => (
              <Grid key={mode} item xs={8} sm={3}>
                <Button variant="contained" fullWidth onClick={startMode(mode)}>
                  {mode}
                </Button>
              </Grid>
            ))
          : 'Loading modes...'}
      </Grid>
    </>
  );
};
