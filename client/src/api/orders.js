import instance from "./getInstanceWithBaseApiUrl";

export const addOrder = async params => {
  let response = await instance.post(`orders/`, params);
  return response.data;
};
export const addDishesToOrder = async params => {
  let response = await instance.post(`dish_in_order/`, params);
  return response.data;
};

export const getOrder = async id => {
  let response = await instance.get(`orders/${id}/`);
  return response.data;
};
