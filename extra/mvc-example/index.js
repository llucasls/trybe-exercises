require('dotenv/config');
const express = require('express');
const bodyParser = require('body-parser');

const authorController = require('./controllers/authorController');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');

app.set('views', './views');

app.get('/authors', authorController.listAuthors);

app.get('/authors/new', authorController.newAuthor);

app.get('/authors/:id', authorController.showAuthor);

app.post('/authors', authorController.createAuthor);

app.use((_req, res) => res.status(404).render('404'));

app.listen(PORT, () => {
  console.log(`Servidor online na porta \x1b[03;94m${PORT}\x1b[00m`);
});
