import { useEffect, useState } from "react";
import axios from "axios";

export type RequestOptions = {
  data?: Record<string, unknown>;
  method: "GET" | "POST";
  params?: Record<string, unknown>;
  url: string;
};

export type RequestGetOptions = RequestOptions & {
  method: "GET";
};

const createRequestBuilder =
  <T>(options: RequestOptions) =>
  async (): Promise<T> => {
    const { data } = await axios<T>(options);

    return data;
  };

export const generateGetHook = <T, D>(
  options: RequestGetOptions,
  defaultTo: D
): (() => T | D) => {
  const getModes = createRequestBuilder<T>(options);

  return () => {
    const [modes, setModes] = useState<T | D>(defaultTo);

    useEffect(() => {
      const process = async () => {
        const modes = await getModes();

        setModes(modes);
      };

      process();
    }, []);

    return modes;
  };
};

const a = <T>(b: T): T => {
  console.log("fzeiofjeozi");

  return "rjfioofjz";
};

const fezfz = a(["hello", { name: "he" }]);
