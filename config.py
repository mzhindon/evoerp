import os

class Config:
    '''SECRET_KES IS USED FOR GENERAL-PURPOSE ENCRYPTION-KEY
       IT IS USED BY WTF FOR CROSS SITE REQUEST FORGUERY(CSRF) PROTECTION
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    '''SQLALCHEMY_RECORD_QUERIES tells Flask-SQLAlchemy to enable the
    recording of query statics'''
    SQLALCHEMY_RECORD_QUERIES = True
    
    '''CLASS METHOD THAT TAKE AN APPLICATION(APP) INSTANCE AS A PARAMETER
       IN CASE WE NEED TO MAKE SPECIFIC CONFIGURATION
       FOR NOW NOW THE METHOD DO ANYTHING '''
    @staticmethod
    def init_app(app):
        pass

'''Config SUBCLASS'''
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://evoerp:devadmin@192.168.1.5/evoerpdev'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://evoerp:devadmin@192.168.1.5/evoerprod'

'''DICTIONARY THAT MANTAIN EACH CONFIGURATION'''
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
