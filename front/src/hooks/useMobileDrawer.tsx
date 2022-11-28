import { useState } from 'react';

const useMobileDrawer = () => {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);

  const toggleDrawer = () => {
    setIsDrawerOpen(!isDrawerOpen);
  };

  return { toggleDrawer, isDrawerOpen };
};

export { useMobileDrawer };
