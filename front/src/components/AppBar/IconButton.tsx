import React from 'react';

import { Box, Button } from '@mui/material';

import { useBreakpoints } from '../../hooks/useBreakpoints';

const makeStyles = (isSmOrBigger: boolean) => ({
  alignItems: 'center',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  marginTop: '2px',
  padding: '5px',
  width: isSmOrBigger ? '100px' : '60px'
});

type Props = {
  icon: React.ReactElement;
  label: string;
  onClick?: () => void;
};

export const IconButton = ({ icon, label, onClick }: Props) => {
  const { isSmOrBigger } = useBreakpoints();

  const styles = makeStyles(isSmOrBigger);

  return (
    <Button sx={{ color: '#fff' }} onClick={onClick}>
      <Box sx={styles}>
        {icon}
        {label}
      </Box>
    </Button>
  );
};
