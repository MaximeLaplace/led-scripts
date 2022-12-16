import React, { useEffect, useState } from 'react';
import axios from 'axios';

import {
  Grid,
  ToggleButton as MuiToggleButton,
  ToggleButtonGroup
} from '@mui/material';
import { styled } from '@mui/material/styles';

import { TitleDivider } from './TitleDivider';

const ToggleButton = styled(MuiToggleButton)({
  color: 'white',
  border: '#666666 1px solid',
  '&.Mui-selected, &.Mui-selected:hover': {
    color: 'white',
    backgroundColor: '#1976d2'
  }
});

type SegmentsOptions = 'top' | 'all';

export const SegmentsToUse = () => {
  const [segmentsToUse, setSegmentsToUse] = useState<SegmentsOptions | null>(
    null
  );

  useEffect(() => {
    const get = async () => {
      const { data } = await axios({
        url: '/segments_to_use',
        method: 'GET'
      });
      setSegmentsToUse(data);
    };
    get();
  }, []);

  const handleChange = (
    event: React.MouseEvent<HTMLElement>,
    newSegmentsToUse: SegmentsOptions
  ) => {
    if (newSegmentsToUse !== null) {
      const oldSegmentsToUse = segmentsToUse;
      setSegmentsToUse(newSegmentsToUse);
      axios({
        url: `/segments_to_use/${newSegmentsToUse}`,
        method: 'POST'
      }).catch(() => {
        setSegmentsToUse(oldSegmentsToUse);
      });
    }
  };

  return (
    segmentsToUse && (
      <>
        <TitleDivider title="Segments to use" />
        <Grid container justifyContent="center" sx={{ marginBottom: '20px' }}>
          <Grid item justifyContent="center">
            <ToggleButtonGroup
              color="primary"
              value={segmentsToUse}
              exclusive
              onChange={handleChange}
            >
              <ToggleButton value="top">Top segments</ToggleButton>
              <ToggleButton value="all">All segments</ToggleButton>
            </ToggleButtonGroup>
          </Grid>
        </Grid>
      </>
    )
  );
};
