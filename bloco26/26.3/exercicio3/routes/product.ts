import { Router } from 'express';
import {
    readAll, createOne, readMany,
    readOne, updateOne, deleteOne,
} from '../controllers/productController';

const productRouter = Router();

productRouter
    .route('/')
    .post(createOne)
    .get(readAll);

productRouter
    .route('/search')
    .get(readMany);

productRouter
    .route('/:id')
    .get(readOne)
    .put(updateOne)
    .delete(deleteOne);

export default productRouter;
