import React from "react";
import { Route } from "src/Router";

export type NavItem = {
  href?: Route;
  icon: React.ReactElement;
  label: string;
  onClick?: () => void;
  position: "left" | "right";
};
