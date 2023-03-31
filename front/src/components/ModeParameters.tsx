import React from "react";

import { createTheme, Grid, ThemeProvider } from "@mui/material";

import { TitleDivider } from "./TitleDivider";

const darkTheme = createTheme({
  palette: {
    mode: "dark"
  }
});

type Props = {
  mode: string | undefined;
};

export const ModeParameters = ({ mode }: Props) => {
  return (
    <>
      <ThemeProvider theme={darkTheme}>
        <TitleDivider title="Parameters" />

        <Grid container justifyContent="center" sx={{ marginBottom: "20px" }}>
          {mode !== undefined ? (
            <Grid item justifyContent="center" sx={{ width: "300px" }}>
              <div>{mode}</div>
            </Grid>
          ) : (
            <Grid item>Loading modes...</Grid>
          )}
        </Grid>
      </ThemeProvider>
    </>
  );
};
