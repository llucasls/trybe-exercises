import App from './app';
import 'dotenv/config';

const app = new App().express;

const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`Ouvindo a porta \x1b[03;94m${port}\x1b[00m!`));
