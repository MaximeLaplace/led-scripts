import {
  generateGetHook,
  generateGetHookWithParams,
  generatePostHook,
  RequestGetOptions,
  RequestPostOptions
} from "./axios";

const GET_REQUEST_PARAMS: Record<string, RequestGetOptions> = {
  modes: {
    url: "/start_mode",
    method: "GET"
  },
  favoriteModes: {
    url: "/favorites",
    method: "GET"
  },
  segmentsToUse: {
    url: "/segments_to_use",
    method: "GET"
  },
  speedFactor: {
    url: "/speed_factor",
    method: "GET"
  }
};

const GET_REQUESTS_WITH_PARAMS: Record<
  string,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  (params: any) => RequestGetOptions
> = {
  modeParameters: (mode: string) => ({
    url: "/mode-parameters",
    method: "GET",
    params: {
      mode
    }
  })
};

const POST_REQUEST_PARAMS: Record<
  string,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  ((data: any) => RequestPostOptions) | RequestPostOptions
> = {
  segmentsToUse: (data: "top" | "all") => ({
    url: `/segments_to_use/${data}`,
    method: "POST"
  }),
  speedFactor: (data: string) => ({
    url: `/speed_factor/${data}`,
    method: "POST"
  }),
  modes: (data: string) => ({
    url: "/start_mode",
    method: "POST",
    data: {
      mode: data
    }
  })
};

export const useModes = generateGetHook<string[]>(GET_REQUEST_PARAMS.modes, []);

export const useFavoriteModes = generateGetHook<string[]>(
  GET_REQUEST_PARAMS.favoriteModes,
  []
);

export const useSegmentsToUse = generateGetHook<"top" | "all" | null>(
  GET_REQUEST_PARAMS.segmentsToUse,
  null
);

export const useSpeedFactor = generateGetHook<string | null>(
  GET_REQUEST_PARAMS.speedFactor,
  null
);

type ModeParameters = Record<
  string,
  string | number | boolean | [number, number, number]
>;

export const useModeParameters = generateGetHookWithParams<
  ModeParameters,
  string
>(GET_REQUESTS_WITH_PARAMS.modeParameters, {});

export const pushSegmentsToUse = generatePostHook<"top" | "all">(
  POST_REQUEST_PARAMS.segmentsToUse
);

export const pushSpeedFactor = generatePostHook<string>(
  POST_REQUEST_PARAMS.speedFactor
);

export const startMode = generatePostHook<string>(POST_REQUEST_PARAMS.modes);
