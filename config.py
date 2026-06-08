from datetime import timedelta



class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=60)
    JWT_SECRET_KEY = "jwt_secret_key"

