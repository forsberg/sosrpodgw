from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap



app = Flask(__name__)
AppConfig(app, "defaultconfig.py")
Bootstrap(app)

import sosrpodgw.views

