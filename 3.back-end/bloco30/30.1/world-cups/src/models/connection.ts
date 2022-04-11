import { connect, ConnectOptions } from 'mongoose';

const dbName = 'world_cups';

const options: ConnectOptions = {
  autoIndex: true,
  dbName,
};

const connection = (host: string, port: string | number) =>
  connect(`mongodb://${host}:${port}/`, options)
    .then((conn) => conn)
    .catch(console.error)

export default connection;
