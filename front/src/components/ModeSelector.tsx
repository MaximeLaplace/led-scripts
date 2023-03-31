import React, { useEffect, useState } from "react";
import { useModes } from "src/queries/requests";

import {
  createTheme,
  Grid,
  MenuItem,
  Select,
  SelectChangeEvent,
  ThemeProvider
} from "@mui/material";

import { TitleDivider } from "./TitleDivider";

const darkTheme = createTheme({
  palette: {
    mode: "dark"
  }
});

type Props = {
  modeToEdit: string | undefined;
  setModeToEdit: (mode: string) => void;
};

const mockModes = () => {
  const [modes, setModes] = useState<string[]>([]);

  useEffect(() => {
    setTimeout(() => {
      setModes(["mode1", "mode2", "mode3", "mode4"]);
    }, 500);
  }, []);

  return modes;
};

export const ModeSelector = ({ modeToEdit, setModeToEdit }: Props) => {
  const [modes] = useModes();
  // const modes = mockModes();

  useEffect(() => {
    setModeToEdit(modes[0]);
  }, [modes]);

  const handleSelectMode = (event: SelectChangeEvent) => {
    setModeToEdit(event.target.value);
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <TitleDivider title="Mode to edit" />

      <Grid container justifyContent="center" sx={{ marginBottom: "20px" }}>
        {modes.length !== 0 ? (
          <Grid item justifyContent="center" sx={{ width: "300px" }}>
            <Select
              fullWidth
              value={modeToEdit}
              onChange={handleSelectMode}
              defaultValue={modes[0]}
            >
              {modes.map((mode) => (
                <MenuItem value={mode} key={mode}>
                  {mode}
                </MenuItem>
              ))}
            </Select>
          </Grid>
        ) : (
          <Grid item>Loading modes...</Grid>
        )}
      </Grid>
    </ThemeProvider>
  );
};
