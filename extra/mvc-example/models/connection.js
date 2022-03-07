const mysql = require('mysql2/promise');
require('dotenv/config');

const {
  MYSQL_USER: user,
  MYSQL_PASSWORD: password,
  MYSQL_DATABASE: database,
  HOST: host,
} = process.env;

module.exports = mysql.createPool({
  host,
  user,
  password,
  database,
});
