import os

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from blueprints import general_blueprint
from blueprints.v1 import (
    users_blueprint,
    categories_blueprint,
)

app = Flask(__name__)

cors = CORS(app, resources={r'/*': {'origins': '*'}})
app.register_blueprint(general_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/v1')
app.register_blueprint(categories_blueprint, url_prefix='/v1')
swagger = Swagger(
    app,
    template_file=os.path.join(
        os.getcwd(),
        'documentation',
        'template.yml',
    ),
)


if __name__ == '__main__':
    app.run()
