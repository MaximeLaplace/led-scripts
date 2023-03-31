import React from "react";
import { createContext, useState } from "react";

export const ROUTES = ["/", "/live", "/favorites"] as const;

export type Route = typeof ROUTES[number];

export const RouteContext = createContext<(route: Route) => void>(() => {
  return;
});

export const RouterProvider = ({
  children
}: {
  children: (route: Route) => React.ReactNode;
}) => {
  const [route, setRoute] = useState<Route>("/");

  return (
    <RouteContext.Provider value={setRoute}>
      {children(route)}
    </RouteContext.Provider>
  );
};
