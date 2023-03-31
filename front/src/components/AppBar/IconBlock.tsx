import React from "react";

import { Box } from "@mui/material";

import { NavItem } from "../../types/drawer";

import { IconButton } from "./IconButton";

type Props = {
  displayLabels?: boolean;
  navItems: Record<string, NavItem[]>;
  position: "left" | "right";
};

const IconBlock = ({ navItems, position, displayLabels = true }: Props) => {
  return (
    <>
      <Box sx={{ flexGrow: 1 }}>
        {navItems.left
          .filter((navItem) => navItem.position === position)
          .map((navItem) => (
            <IconButton
              key={navItem.label}
              label={displayLabels ? navItem.label : ""}
              icon={navItem.icon}
              href={navItem.href}
            />
          ))}
      </Box>
      <Box>
        {navItems.right
          .filter((navItem) => navItem.position === position)
          .map((navItem) => (
            <IconButton
              key={navItem.label}
              label={displayLabels ? navItem.label : ""}
              icon={navItem.icon}
              href={navItem.href}
            />
          ))}
      </Box>
    </>
  );
};

export { IconBlock };
