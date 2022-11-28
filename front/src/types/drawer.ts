import React from 'react';

export type NavItem = {
  icon: React.ReactElement;
  label: string;
  position: 'left' | 'right';
};
