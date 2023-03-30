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

export type RequestPostOptions = RequestOptions & {
  method: "POST";
};

const createRequestRunner =
  <T>(options: RequestOptions) =>
  async (): Promise<T> => {
    const { data } = await axios<T>(options);

    return data;
  };

export const generateGetHook = <InboundDataType>(
  options: RequestGetOptions,
  defaultTo: InboundDataType
): (() => [InboundDataType, React.Dispatch<InboundDataType>]) => {
  const request = createRequestRunner<InboundDataType>(options);

  return () => {
    const [data, setData] = useState<InboundDataType>(defaultTo);

    useEffect(() => {
      const process = async () => {
        const axiosData = await request();

        setData(axiosData);
      };

      process();
    }, []);

    return [data, setData];
  };
};

export const generatePostHook =
  <OutboundDataType>(
    options:
      | RequestPostOptions
      | ((data: OutboundDataType) => RequestPostOptions)
  ) =>
  async (data: OutboundDataType) => {
    const parsedOptions =
      typeof options === "function" ? options(data) : options;

    return createRequestRunner(parsedOptions)();
  };
