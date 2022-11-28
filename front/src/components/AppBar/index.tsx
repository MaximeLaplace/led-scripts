import React from 'react';

import { NavItem } from '@ledapp/types/drawer';
import AppsIcon from '@mui/icons-material/Apps';
import MenuIcon from '@mui/icons-material/Menu';
import SettingsIcon from '@mui/icons-material/Settings';
import TuneIcon from '@mui/icons-material/Tune';
import { Fab } from '@mui/material';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';

import { useBreakpoints } from '../../hooks/useBreakpoints';
import { useMobileDrawer } from '../../hooks/useMobileDrawer';

import { IconBlock } from './IconBlock';
import { MobileDrawer } from './MobileDrawer';

const NAV_ITEMS: NavItem[] = [
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
    icon: <SettingsIcon />,
    label: 'SETTINGS',
    position: 'right'
  }
];

const AppBar = () => {
  const { isDrawerOpen, toggleDrawer } = useMobileDrawer();

  const { isSmOrBigger } = useBreakpoints();

  return isSmOrBigger ? (
    <MuiAppBar component="nav" sx={{ background: '#232323' }}>
      <Toolbar>
        <IconBlock navItems={NAV_ITEMS} position="left" />
        <IconBlock navItems={NAV_ITEMS} position="right" />
      </Toolbar>
    </MuiAppBar>
  ) : (
    <>
      <Fab
        aria-label="menu"
        sx={{
          position: 'fixed',
          margin: 4,
          bottom: '10px',
          backgroundColor: '#232323'
        }}
        color="info"
        onClick={toggleDrawer}
      >
        <MenuIcon />
      </Fab>
      <MobileDrawer
        isOpen={isDrawerOpen}
        navItems={NAV_ITEMS}
        toggleDrawer={toggleDrawer}
      />
    </>
  );
};

export { AppBar };
