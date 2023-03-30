import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import { Toolbar } from "@mui/material";
import Box from "@mui/material/Box";

import { AppBar } from "./components/AppBar";
import { Dashboard } from "./pages/Dashboard";
import { IndividualMode } from "./pages/IndividualMode";

import "./App.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Dashboard />
  },
  {
    path: "/live",
    element: <IndividualMode />
  },
  {
    path: "*",
    element: (
      <div>
        404
        <br /> Page does not exist
      </div>
    )
  }
]);

const App: React.FC = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <AppBar />
      <Box component="main" sx={{ p: 3 }}>
        <Toolbar />

        <RouterProvider router={router} />
      </Box>
    </Box>
  );
};

export { App };
