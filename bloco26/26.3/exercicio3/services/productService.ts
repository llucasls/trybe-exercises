import Product from '../models/product';

const readAll = async () => {
    const products = Product.findAll();
    return products;
};

const createOne = async (product: any) => {
    await Product.create(product);
    const result = Product.findOne(product);
    return result;
};

const readMany = async () => {};

const readOne = async () => {};

const updateOne = async () => {};

const deleteOne = async () => {};

export default {
    readAll, createOne, readMany,
    readOne, updateOne, deleteOne,
}
