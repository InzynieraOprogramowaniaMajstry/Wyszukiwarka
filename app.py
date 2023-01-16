import sys
import os
from initialize_objects import app
from controllers_and_routes.all_routes import user_bp
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(SCRIPT_DIR)

app.register_blueprint(user_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
