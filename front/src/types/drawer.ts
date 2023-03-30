import React from "react";

export type NavItem = {
  href?: string;
  icon: React.ReactElement;
  label: string;
  onClick?: () => void;
  position: "left" | "right";
};
