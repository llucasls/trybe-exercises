require('dotenv/config');
const mysql = require('mysql2/promise');

const { MYSQL_USER: user, MYSQL_PASSWORD: password, MYSQL_HOST: host } = process.env;
const database = 'model_example';

module.exports = mysql.createPool({ user, host, password, database });
