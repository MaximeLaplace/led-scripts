import React from "react";
import { pushSpeedFactor, useSpeedFactor } from "src/queries/requests";

import {
  Button,
  createTheme,
  Grid,
  TextField,
  ThemeProvider
} from "@mui/material";

import { TitleDivider } from "./TitleDivider";

const darkTheme = createTheme({
  palette: {
    mode: "dark"
  }
});

export const SpeedFactor = () => {
  const [speedFactor, setSpeedFactor] = useSpeedFactor();

  const handleChange = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setSpeedFactor(event.currentTarget.value);
  };

  const handleSubmit = () => {
    if (
      speedFactor !== null &&
      parseFloat(speedFactor).toString() === speedFactor
    ) {
      pushSpeedFactor(speedFactor);
    }
  };

  return (
    <>
      <ThemeProvider theme={darkTheme}>
        <TitleDivider title="Speed Factor" />
        <Grid container justifyContent="center" sx={{ marginBottom: "20px" }}>
          {speedFactor !== null ? (
            <Grid item justifyContent="center">
              <div>
                <TextField
                  label="Speed factor"
                  id="outlined-size-small"
                  defaultValue={speedFactor}
                  size="small"
                  onChange={handleChange}
                  sx={{
                    marginRight: "20px"
                  }}
                />
                <Button variant="contained" onClick={handleSubmit}>
                  GO
                </Button>
              </div>
            </Grid>
          ) : (
            <Grid item>Loading speed factor...</Grid>
          )}
        </Grid>
      </ThemeProvider>
    </>
  );
};
