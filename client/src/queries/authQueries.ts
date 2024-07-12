import axios from "axios";

export const AUTH_QUERIE = async (
  login: string,
  password: string,
  email: string,
  endpoint: string
) => {
  return await axios
    .post(`/${endpoint}/${login}/${password}${email ? `/${email}` : ""}`)
    .then((res) => {
      return res.data as string;
    });
};
