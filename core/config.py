from os.path import abspath, dirname

base_dir = abspath(dirname(__file__)) + '/..'
print(base_dir,"BASEDIR")


class BaseConfig:
    SECRET_KEY = '13@$skireghllqwertedbeighdfngs$5$455##@'
    DEBUG = True
    # MongoDb
    MONGODB_DB = 'online_test'
    FLASK_ADMIN_SWATCH = 'cerulean'
    # flask_json
    JSON_ADD_STATUS = False
    JSON_DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'
    MONGODB_SETTINGS = {
        'db': 'online_test',
        'host': 'mongodb://localhost/online_test',
        'connect': False,
    }
class DebugConfig(BaseConfig):
    pass