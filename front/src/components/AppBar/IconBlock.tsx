import React from 'react';

import { Box, Button } from '@mui/material';

import { NavItem } from '../../types/drawer';

const styles = {
  alignItems: 'center',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  marginTop: '2px',
  padding: '5px',
  width: '100px'
};

type Props = {
  navItems: NavItem[];
  position: 'left' | 'right';
};

const IconBlock = ({ navItems, position }: Props) => (
  <Box sx={{ flexGrow: position === 'left' ? 1 : 0 }}>
    {navItems
      .filter((navItem) => navItem.position === position)
      .map((navItem) => (
        <Button key={navItem.label} sx={{ color: '#fff' }}>
          <Box sx={styles}>
            {navItem.icon}
            {navItem.label}
          </Box>
        </Button>
      ))}
  </Box>
);

export { IconBlock };
