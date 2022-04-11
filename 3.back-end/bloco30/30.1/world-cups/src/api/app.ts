import 'dotenv/config';
import express from 'express';
import router from '../routes';
import connection from '../models/connection';

const host = process.env.HOST || '127.0.0.1';
const port = process.env.PORT || 3000;
type MongooseConnection = typeof import('mongoose') | void;

class App {
  public express: express.Application;

  public connection: Promise<MongooseConnection>;

  constructor() {
    this.express = express();
    this.connection = connection(host, port);
    this.middlewares();
    this.routes();
  }

  private middlewares(): void {
    this.express.use(express.json());
  }

  private routes() {
    this.express.use(router);
  }
}

export default App;
