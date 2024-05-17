import sys

from flask import Flask

from database.database import db
from flask_cors import CORS
from routes import pedidos

app = Flask(__name__)

# CORS Configs
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Database Configs
db.init_app(app)

# Registering Blueprints
app.register_blueprint(pedidos.api_blueprint)

# Create the database if the command line argument is "create_db"
if len(sys.argv) > 1 and sys.argv[1] == "create_db":
    with app.app_context():
        db.create_all()
    print("Database created successfully")
    sys.exit(0)

# Run the application
if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0", port=5000)
