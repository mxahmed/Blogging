
import imp
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import App, db
import os.path
import sys

if __name__ == "__main__":

    command = sys.argv[1]
    if command in ['createdb', 'mkmigrations', 'migrate', 'run']:
        if command == 'createdb':
            db.create_all()
            if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
                api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
                api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            else:
                api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

            print("DataBase Created")

        elif command == 'mkmigrations':
            v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
            tmp_module = imp.new_module('old_model')
            old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            exec(old_model, tmp_module.__dict__)
            script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
            open(migration, "wt").write(script)
            #api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            print('New migration saved as ' + migration)
            print('Current database version: ' + str(v))

        elif command == "migrate":
            api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
            
        elif command == 'run':
            App.run(debug=True)
    else:
        print('Wrong Command')
