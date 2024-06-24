# server/app.py

import os
from flask import Flask
from flask_migrate import Migrate
from models import db

# Function to create and configure the Flask application
def create_app():
    app = Flask(__name__)

    # Configure the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Initialize migration management
    Migrate(app, db)

    # Register blueprints here if the application grows
    # from .views import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app

# Create the application instance
app = create_app()

# Set up logging
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting the application...')

    # Run the application
    try:
        app.run(port=5555, debug=True)
    except Exception as e:
        logging.error(f"Error running the application: {e}")
