import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
#SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://dbname_769a_user:fdYappUIOpdhxeMYQcAibJ8wKeNJzQ7E@dpg-ctuihcdds78s73fogt6g-a.frankfurt-postgres.render.com/dbname_769a'
SQLALCHEMY_TRACK_MODIFICATIONS=False


