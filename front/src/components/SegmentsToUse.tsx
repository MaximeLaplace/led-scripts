import React from "react";
import { pushSegmentsToUse, useSegmentsToUse } from "src/queries/requests";

import {
  Grid,
  ToggleButton as MuiToggleButton,
  ToggleButtonGroup
} from "@mui/material";
import { styled } from "@mui/material/styles";

import { TitleDivider } from "./TitleDivider";

const ToggleButton = styled(MuiToggleButton)({
  color: "white",
  border: "#666666 1px solid",
  "&.Mui-selected, &.Mui-selected:hover": {
    color: "white",
    backgroundColor: "#1976d2"
  }
});

type SegmentsOptions = "top" | "all";

export const SegmentsToUse = () => {
  const [segmentsToUse, setSegmentsToUse] = useSegmentsToUse();

  const handleChange = (
    event: React.MouseEvent<HTMLElement>,
    newSegmentsToUse: SegmentsOptions
  ) => {
    if (newSegmentsToUse !== null) {
      setSegmentsToUse(newSegmentsToUse);
      pushSegmentsToUse(newSegmentsToUse);
    }
  };

  return (
    <>
      <TitleDivider title="Segments to use" />
      <Grid container justifyContent="center" sx={{ marginBottom: "20px" }}>
        {segmentsToUse ? (
          <Grid item justifyContent="center">
            <ToggleButtonGroup
              color="primary"
              value={segmentsToUse}
              exclusive
              onChange={handleChange}
            >
              <ToggleButton value="top">Top segments</ToggleButton>
              <ToggleButton value="all">All segments</ToggleButton>
            </ToggleButtonGroup>
          </Grid>
        ) : (
          <Grid item>Loading segments...</Grid>
        )}
      </Grid>
    </>
  );
};
