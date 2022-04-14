import { Router } from 'express';
import WorldCupController from '../controllers/worldcup';

const worldCupRouter = Router();
const { readAll } = new WorldCupController();

worldCupRouter.get('/', readAll);

export default worldCupRouter;
