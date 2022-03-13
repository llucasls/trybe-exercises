import 'dotenv/config';
import { MongoClient } from 'mongodb'

const MONGO_DB_URL: string = `mongodb://${process.env.HOST || 'mongodb'}:27017`;
const DB_NAME: string = `${process.env.DB_NAME}`;

const mongoClientConfig: object = {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}

const connection = () => (
    MongoClient
        .connect(MONGO_DB_URL, mongoClientConfig)
        .then((conn) => conn.db(DB_NAME))
        .catch((err) => {
            console.error(err.message);
            process.exit(1);
    })
);

export { connection };
