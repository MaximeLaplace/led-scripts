import React, { useContext } from "react";
import { Route, RouteContext } from "src/Router";

import { Box, Button } from "@mui/material";

import { useBreakpoints } from "../../hooks/useBreakpoints";

const makeStyles = (isSmOrBigger: boolean) => ({
  alignItems: "center",
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  marginTop: "2px",
  padding: "5px",
  width: isSmOrBigger ? "100px" : "60px"
});

type Props = {
  href?: Route;
  icon: React.ReactElement;
  label: string;
};

export const IconButton = ({ icon, label, href }: Props) => {
  const { isSmOrBigger } = useBreakpoints();

  const setRoute = useContext(RouteContext);

  const styles = makeStyles(isSmOrBigger);

  return (
    <Button
      sx={{ color: "#fff" }}
      onClick={() => {
        setRoute(href || "/");
      }}
    >
      <Box sx={styles}>
        {icon}
        {label}
      </Box>
    </Button>
  );
};
