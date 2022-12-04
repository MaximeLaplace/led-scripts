import React from 'react';

import { NavItem } from '@ledapp/types/drawer';
import AppsIcon from '@mui/icons-material/Apps';
import FlashOnIcon from '@mui/icons-material/FlashOn';
import LogoutIcon from '@mui/icons-material/Logout';
import MenuIcon from '@mui/icons-material/Menu';
import TuneIcon from '@mui/icons-material/Tune';
import { Fab } from '@mui/material';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';

import { useBreakpoints } from '../../hooks/useBreakpoints';
import { useMobileDrawer } from '../../hooks/useMobileDrawer';

import { IconBlock } from './IconBlock';
import { IconButton } from './IconButton';
import { MobileDrawer } from './MobileDrawer';

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
  const { isDrawerOpen, toggleDrawer } = useMobileDrawer();

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
  // <>
  //   <Fab
  //     aria-label="menu"
  //     sx={{
  //       position: 'fixed',
  //       margin: 4,
  //       bottom: '10px',
  //       backgroundColor: '#232323'
  //     }}
  //     color="info"
  //     onClick={toggleDrawer}
  //   >
  //     <MenuIcon />
  //   </Fab>
  // </>
  // );
};

export { AppBar };
