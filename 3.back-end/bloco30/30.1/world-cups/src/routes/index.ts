import { Router } from 'express';
import worldCupRouter from './worldcup';

const router = Router();

router.use('/', worldCupRouter);

export default router;
