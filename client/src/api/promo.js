import instance from "./getInstanceWithBaseApiUrl";

export const getPromo = async () => {
  let response = await instance.get(`promo/`);
  return response.data["results"];
};
