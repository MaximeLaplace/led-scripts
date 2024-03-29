import React from "react";

import { Modes } from "../components/Modes";
import { RebootSite } from "../components/RebootSite";
import { SegmentsToUse } from "../components/SegmentsToUse";
import { SpeedFactor } from "../components/SpeedFactor";

const Dashboard = () => {
  return (
    <>
      <SegmentsToUse />

      <SpeedFactor />

      <Modes />

      <RebootSite />
    </>
  );
};

export { Dashboard };
