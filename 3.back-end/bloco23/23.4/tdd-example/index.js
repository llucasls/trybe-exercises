const express = require('express');
const bodyParser = require('body-parser');

const MovieController = require('./src/controllers/movieController');

const app = express();

app.use(bodyParser.json());

app.post('/movies', MovieController.create);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Ouvindo a porta \x1b[03;92m${PORT}\x1b[00m`);
});
