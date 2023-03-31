import React, { useCallback, useEffect } from "react";
import { useModeParameters } from "src/queries/requests";

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

const DISCARDED_PARAMS = [
  "duration_s",
  "durations_s",
  "duration",
  "durations",
  "infinite"
];
type ParamValue = string | number | boolean | [number, number, number];

type FormFieldProps = {
  name: string;
  setParam: (
    newValue: string | number | boolean | [number, number, number]
  ) => void;
  value: ParamValue;
};

const FormField = ({ name, value, setParam }: FormFieldProps) => {
  if (DISCARDED_PARAMS.includes(name)) {
    return <></>;
  }

  const handleChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
      console.log("handleChange !");
      if (event.currentTarget) {
        setParam(parseInt(event.currentTarget.value));
      }
    },
    [name]
  );

  if (typeof value === "number") {
    return (
      <TextField
        label={name}
        id="outlined-size-small"
        defaultValue={value.toString()}
        size="small"
        onChange={handleChange}
        sx={{
          marginRight: "20px"
        }}
      />
    );
  }

  return (
    <div>
      {name}: {JSON.stringify(value)}
    </div>
  );
};

type Props = {
  mode: string;
};

export const ModeParameters = ({ mode }: Props) => {
  const [modeParameters, setModeParameters] = useModeParameters(mode);

  useEffect(() => {
    console.log({ modeParameters });
  }, [modeParameters]);

  const handleSubmit = () => {
    return;
  };

  return (
    <>
      <ThemeProvider theme={darkTheme}>
        <TitleDivider title="Parameters" />

        <Grid container justifyContent="center" sx={{ marginBottom: "20px" }}>
          {mode !== undefined ? (
            <Grid item justifyContent="center" sx={{ width: "300px" }}>
              {Object.entries(modeParameters).map(
                ([paramName, paramDefault]) => {
                  console.log(paramName, paramDefault);

                  return (
                    <div key={paramName} style={{ marginBottom: "30px" }}>
                      <FormField
                        name={paramName}
                        value={paramDefault}
                        setParam={(newValue) =>
                          setModeParameters((current) => ({
                            ...current,
                            [paramName]: newValue
                          }))
                        }
                      />
                    </div>
                  );
                }
              )}

              <Button variant="contained" onClick={handleSubmit}>
                GO
              </Button>
            </Grid>
          ) : (
            <Grid item>Loading modes...</Grid>
          )}
        </Grid>
      </ThemeProvider>
    </>
  );
};
