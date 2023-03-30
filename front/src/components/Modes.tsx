import React from "react";
import { startMode, useModes } from "src/queries/requests";

import { Button, Grid } from "@mui/material";

import { TitleDivider } from "./TitleDivider";

export const Modes = () => {
  const [modes] = useModes();

  return (
    <>
      <TitleDivider title="Modes" />
      <Grid container spacing={4} justifyContent="center">
        {modes.length ? (
          modes.map((mode) => (
            <Grid key={mode} item xs={8} sm={3}>
              <Button
                variant="contained"
                fullWidth
                onClick={() => startMode(mode)}
              >
                {mode}
              </Button>
            </Grid>
          ))
        ) : (
          <Grid item>Loading modes...</Grid>
        )}
      </Grid>
    </>
  );
};
