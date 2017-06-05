from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_pyfile('config.py')
Bootstrap(app)

import webapp.views

if __name__ == "__main__":
    app.run()
