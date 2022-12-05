import { AxiosResponse } from 'axios';

type CustomPromise<T, D> = Promise<AxiosResponse<T, D>> & {
  data: () => T | null;
  isFulfilled: () => boolean;
  isPending: () => boolean;
  isRejected: () => boolean;
};

export const handleAxiosRequest = <T, D = unknown>(
  promise: Promise<AxiosResponse<T, D>>
) => {
  let isPending = true;
  let isRejected = false;
  let isFulfilled = false;
  let data: T | null = null;

  const result = (promise as CustomPromise<T, D>).then(
    (v) => {
      isFulfilled = true;
      isPending = false;
      data = v.data;
      return v;
    },
    (e) => {
      isRejected = true;
      isPending = false;
      throw e;
    }
  ) as CustomPromise<T, D>;

  result.isFulfilled = () => isFulfilled;
  result.isPending = () => isPending;
  result.isRejected = () => isRejected;
  result.data = () => data;
  return result;
};
