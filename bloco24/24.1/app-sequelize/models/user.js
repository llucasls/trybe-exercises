const User = (sequelize, Datatypes) => {
  const User = sequelize.define("User", {
    fullname: DataTypes.STRING,
    email: DataTypes.STRING,
    phone_num: DataTypes.STRING,
  });

  return User;
};

module.exports = User;
