require('dotenv').config();

const {
  MYSQL_USER: username,
  MYSQL_HOST: host,
  MYSQL_PASSWORD: password,
} = process.env;
const dialect = 'mysql';

const config = { username, password, host, dialect };

module.exports = {
  development: {
    ...config,
    database: 'jwt_exercise_dev'
  },
  test: {
    ...config,
    database: 'jwt_exercise_test'
  },
  production: {
    ...config,
    database: 'jwt_exercise'
  },
};
