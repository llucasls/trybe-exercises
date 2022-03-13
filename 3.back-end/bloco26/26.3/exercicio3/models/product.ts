import { ObjectId } from 'mongodb';
import { connection } from './connections';

const findAll = async () => {
    const newConnection = await connection();
    const productsList = await newConnection
        .collection('products').find().toArray();
    return productsList;
};

const findOne = async (filter: object) => {
    const newConnection = await connection();
    const product = await newConnection
        .collection('products').findOne(filter);
    return product;
}

const create = async (product: any): Promise<void> => {
    const newConnection = await connection();
    await newConnection.collection('products').insertOne(product);
};

const findById = () => {
};

const update = () => {
};

const destroy = () => {
};

/* const findProductByName = async (name) => {
  const newConnection = await connection();
  const product = await newConnection
    .collection('products').findOne({ name });
  return product;
};

const findProductById = async (id) => {
  try {
    const productId = new ObjectId(id);
    const newConnection = await connection();
    const product = await newConnection
      .collection('products').findOne(productId);
    return product;
  } catch (err) {
    return { err: {
      code: 'invalid_data',
      message: 'Wrong id format',
    } };
  }
};

const updateProduct = async (id, name, quantity) => {
  try {
    const productId = new ObjectId(id);
    const newConnection = await connection();
    await newConnection.collection('products')
      .updateOne({ _id: productId }, { $set: { name, quantity } });
    const product = await newConnection.collection('products')
      .findOne(productId);
    return product;
  } catch (err) {
    return { err: {
      code: 'invalid_data',
      message: 'Wrong id format',
    } };
  }
};

const deleteProduct = async (id) => {
  try {
    const productId = new ObjectId(id);
    const newConnection = await connection();
    const product = await newConnection.collection('products')
      .findOne(productId);
    await newConnection.collection('products').deleteOne({ _id: productId });
    return product;
  } catch (err) {
    return { err: {
      code: 'invalid_data',
      message: 'Wrong id format',
      status: 422,
    } };
  }
}; */

export default {
    findAll, findOne, create,
}
