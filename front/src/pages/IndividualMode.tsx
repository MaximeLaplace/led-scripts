import React, { useState } from "react";

import { ModeParameters } from "../components/ModeParameters";
import { ModeSelector } from "../components/ModeSelector";

const IndividualMode = () => {
  const [modeToEdit, setModeToEdit] = useState<string | undefined>(undefined);

  return (
    <>
      <ModeSelector modeToEdit={modeToEdit} setModeToEdit={setModeToEdit} />
      <ModeParameters mode={modeToEdit} />
    </>
  );
};

export { IndividualMode };
