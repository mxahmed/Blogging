import os

# gets the projects dir
basdir = os.path.abspath(os.path.dirname('__file__'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basdir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basdir, 'migrations')

WTF_CSFR_ENABLED = True
SECRET_KEY = "this-my-secret-key"
