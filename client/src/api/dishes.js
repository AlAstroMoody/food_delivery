import instance from "./getInstanceWithBaseApiUrl";

export const getDishes = async () => {
  let response = await instance.get(`dishes/`);
  return response.data["results"];
};

export const getCategories = async () => {
  let response = await instance.get(`category/`);
  return response.data["results"];
};
