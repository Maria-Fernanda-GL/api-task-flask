class Config:
    DATABASE_DEV = 'task_flask'
    DATABASE_TEST = 'task_flask_test'
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = '123456'


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ Config.DATABASE_USER }:{ Config.DATABASE_PASSWORD }@localhost/{ Config.DATABASE_TEST }'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ Config.DATABASE_USER }:{ Config.DATABASE_PASSWORD }@localhost/{ Config.DATABASE_DEV }'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
}
