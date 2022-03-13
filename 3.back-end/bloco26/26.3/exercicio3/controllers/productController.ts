import { Request, Response } from 'express';
import service from '../services/productService';

const readAll = async (req: Request, res: Response) => {
    try {
        const products = await service.readAll();
        return res.status(200).json(products);
    } catch (err: any) {
        return res.status(err.status).send({ message: err.message });
    }
}

const createOne = async (req: Request, res: Response) => {
    try {
        const product = req.body;
        const result = await service.createOne(product);
        return res.status(201).json(product);
    } catch (err: any) {
        return res.status(err.status).send({ message: err.message });
    }
}

const readMany = async (req: Request, res: Response) => {
    try {
    } catch (err: any) {
        return res.status(err.status).send({ message: err.message });
    }
}

const readOne = async (req: Request, res: Response) => {
    try {
    } catch (err: any) {
        return res.status(err.status).send({ message: err.message });
    }
}

const updateOne = async (req: Request, res: Response) => {
    try {
    } catch (err: any) {
        return res.status(err.status).send({ message: err.message });
    }
}

const deleteOne = async (req: Request, res: Response) => {
    try {
    } catch (err: any) {
        return res.status(err.status).send({ message: err.message });
    }
}

export {
    readAll, createOne, readMany,
    readOne, updateOne, deleteOne,
}
