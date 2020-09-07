import instance from "./getInstanceWithBaseApiUrl";

export const editProfile = async params => {
  let response = await instance.patch(`profile/${params.get("user")}/`, params);
  return response.data;
};

export const getProfile = async id => {
  let response = await instance.get(`profile/${id}/`);
  return response.data;
};
