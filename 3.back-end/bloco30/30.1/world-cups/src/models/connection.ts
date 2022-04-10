import { connect, ConnectOptions } from 'mongoose';
import 'dotenv/config';

const host = process.env.HOST || '127.0.0.1';
const port = process.env.PORT || '3000';
const dbName = 'world_cups';

const options: ConnectOptions = {
  autoIndex: true,
  dbName,
};

const connection = connect(`mongodb://${host}:${port}/`, options);

export default connection;
