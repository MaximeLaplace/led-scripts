import axios from 'axios';

import { handleAxiosRequest } from './promiseHandler';

export const useModes = () => {
  const options = {
    url: 'http://127.0.0.1:5000/start_mode',
    method: 'GET'
  };

  const { data, isFulfilled, isPending, isRejected } = handleAxiosRequest<
    string[]
  >(axios(options));

  return {
    data,
    isFulfilled,
    isPending,
    isRejected
  };
};
