import { generateGetHook, RequestGetOptions } from "./axios";

const GET_REQUEST_PARAMS: Record<string, RequestGetOptions> = {
  modes: {
    url: "http://127.0.0.1:5000/start_mode",
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

export const requests = {
  getModes: generateGetHook<string[]>(GET_REQUEST_PARAMS.modes, []),
  getSegmentsToUse: generateGetHook<"top" | "all">(
    GET_REQUEST_PARAMS.segmentToUse
  ),
  getSpeedFactor: generateGetHook<string>(GET_REQUEST_PARAMS.getSpeedFactor)
};
