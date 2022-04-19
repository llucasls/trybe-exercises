import FrameController from './controllers/frame';
import LensController from './controllers/lens';
import Frame from './interfaces/frame';
import Lens from './interfaces/lens';
import CustomRouter from './routes/router';
import App from './server';

const server = new App();

const lensController = new LensController();
const frameController = new FrameController();

const lensRouter = new CustomRouter<Lens>();
lensRouter.addRoute(lensController);

const frameRouter = new CustomRouter<Frame>();
frameRouter.addRoute(frameController);

server.addRouter(lensRouter.router);
server.addRouter(frameRouter.router);

server.startServer();
