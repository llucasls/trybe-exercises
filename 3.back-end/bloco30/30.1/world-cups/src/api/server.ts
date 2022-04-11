import App from './app';
import 'dotenv/config';

const { express: app } = new App();

const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`Ouvindo a porta \x1b[03;94m${port}\x1b[00m!`));
