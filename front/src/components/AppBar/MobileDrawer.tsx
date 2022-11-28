import React from 'react';

import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';

import { NavItem } from '../../types/drawer';

type Props = {
  isOpen: boolean;
  navItems: NavItem[];
  toggleDrawer: () => void;
};

const MobileDrawer = ({ navItems, isOpen, toggleDrawer }: Props) => {
  return (
    <Box component="nav">
      <Drawer
        variant="temporary"
        open={isOpen}
        onClose={toggleDrawer}
        ModalProps={{
          keepMounted: true // Better open performance on mobile.
        }}
        sx={{
          display: { xs: 'block', sm: 'none' },
          '& .MuiDrawer-paper': {
            boxSizing: 'border-box',
            width: '75%'
          },
          backgroundColor: '#232323'
        }}
      >
        <Box
          onClick={toggleDrawer}
          sx={{
            textAlign: 'center',
            background: '#232323',
            height: '100vh',
            color: 'white'
          }}
        >
          <Typography variant="h6" sx={{ my: 2 }}>
            APPLI LED
          </Typography>
          <Divider sx={{ bgcolor: 'lightgrey' }} />
          <List sx={{ background: '#232323' }}>
            {navItems.map((navItem) => (
              <ListItem key={navItem.label} disablePadding>
                <ListItemButton sx={{ textAlign: 'center' }}>
                  {navItem.icon}
                  <ListItemText primary={navItem.label} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>
    </Box>
  );
};

export { MobileDrawer };
