from flask import Flask
from clear_my_record_backend.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

cmr = Flask(__name__)
cmr.config.from_object(Config)
dbs = SQLAlchemy(cmr)
migratate = Migrate(cmr, dbs)
CORS(cmr)

# having this import here is key to avoid circular imports, sorry pep8
from clear_my_record_backend.server import routes, models
