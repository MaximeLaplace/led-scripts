import React from "react";

import { Toolbar } from "@mui/material";
import Box from "@mui/material/Box";

import { AppBar } from "./components/AppBar";
import { Dashboard } from "./pages/Dashboard";
import { IndividualMode } from "./pages/IndividualMode";
import { Route, RouterProvider, ROUTES } from "./Router";

import "./App.css";

const router: Record<Route, React.ReactElement> = {
  "/": <Dashboard />,
  "/live": <IndividualMode />
};

const Router = ({ route }: { route: Route }) => {
  if (!ROUTES.includes(route)) {
    return (
      <div>
        404
        <br /> Page does not exist
      </div>
    );
  }

  // eslint-disable-next-line security/detect-object-injection
  const element = router[route];

  return element;
};

const App: React.FC = () => {
  return (
    <RouterProvider>
      {(route) => (
        <>
          <Box sx={{ display: "flex", width: "100vw" }}>
            <AppBar />
            <Box component="main" sx={{ p: 3, width: "100%" }}>
              <Toolbar />

              <Router route={route} />
            </Box>
          </Box>
        </>
      )}
    </RouterProvider>
  );
};

export { App };
