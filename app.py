import os

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from blueprints import general_blueprint

app = Flask(__name__)

cors = CORS(app, resources={r'/*': {'origins': '*'}})
app.register_blueprint(general_blueprint)
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
