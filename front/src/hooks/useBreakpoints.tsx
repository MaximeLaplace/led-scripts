import { useMediaQuery, useTheme } from '@mui/material';

const useBreakpoints = () => {
  const theme = useTheme();
  const isSmOrBigger = useMediaQuery(theme.breakpoints.up('sm'));

  return { isSmOrBigger };
};

export { useBreakpoints };
