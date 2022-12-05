import React from 'react';

import { NavItem } from '@ledapp/types/drawer';
import AppsIcon from '@mui/icons-material/Apps';
import FlashOnIcon from '@mui/icons-material/FlashOn';
import LogoutIcon from '@mui/icons-material/Logout';
import TuneIcon from '@mui/icons-material/Tune';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';

import { useBreakpoints } from '../../hooks/useBreakpoints';

import { IconBlock } from './IconBlock';

const NAV_ITEMS: Record<string, NavItem[]> = {
  left: [
    {
      icon: <TuneIcon />,
      label: 'LIVE',
      position: 'left'
    },
    {
      icon: <AppsIcon />,
      label: 'PRESETS',
      position: 'left'
    },
    {
      icon: <FlashOnIcon />,
      label: 'STROBO',
      position: 'left'
    }
  ],
  right: [
    {
      icon: <LogoutIcon />,
      label: 'LOGOUT',
      position: 'right'
    }
  ]
};

const AppBar = () => {
  const { isSmOrBigger } = useBreakpoints();

  return (
    <MuiAppBar component="nav" sx={{ background: '#232323' }}>
      <Toolbar>
        <>
          <IconBlock
            navItems={NAV_ITEMS}
            position="left"
            displayLabels={isSmOrBigger}
          />
          <IconBlock
            navItems={NAV_ITEMS}
            position="right"
            displayLabels={isSmOrBigger}
          />
        </>
      </Toolbar>
    </MuiAppBar>
  );
};

export { AppBar };
