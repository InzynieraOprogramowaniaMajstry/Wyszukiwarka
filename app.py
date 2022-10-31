import sys
import os
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(SCRIPT_DIR)

from initialize_objects import app
from controllers_and_routes.all_routes import user_bp

app.register_blueprint(user_bp, url_prefix='/')

#cli commands
from cli_commands import register
register(app)

if __name__ == '__main__':
    app.run(debug=True)