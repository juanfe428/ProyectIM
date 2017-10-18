import os
class Config(object):
	SECRET_KEY='clave secreta'
class DevelopmentConfig(Config):
	DEBUG=True
	SQLALCHEMY_DATABASE_URI='mysql://root:juanfesa123@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS=True
	