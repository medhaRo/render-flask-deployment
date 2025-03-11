import os
from flask import Flask
from file_api import file_api

# Create the main Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(file_api)

if __name__ == '__main__':
    # Use PORT from the environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
