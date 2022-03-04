import 'dotenv/config';
import express, { Request, Response } from 'express';
import router from './routes';

const app: express.Application = express();

const PORT: number = Number(process.env.PORT) || 8000;

app.use(express.json());
app.use(router);

app.get('/', (req: Request, res: Response) => {
    res.send({ message: 'Trybescript Guitar Store Online!' });
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
