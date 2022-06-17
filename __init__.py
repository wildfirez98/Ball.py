# Import Flask framework
from flask import Flask
from flask_migrate import Migrate # Import Migrate tool from package Flask-Migrate so we can migrate our models on the command line

# Create the Application Factory
def create_app():
    # Create the app instance
    app = Flask(__name__)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password1234@localhost:5432/reptile_zoo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    from . import models # Import model.py so we can access 'db' variable
    models.db.init_app(app) # We now have access to all the built-in SQLAlchemy class methods through models.db. Call the init_app method on it and pass it the app instance.
    migrate = Migrate(app, models.db) # Create migrate variable

    # Routes

    @app.route('/')
    def hello():
        return "Hello, Reptile Zoo!"

# Register pet blueprint endpoint
    from . import reptiles
    app.register_blueprint(reptiles.bp) # Pointing to reptiles.py on same file level



    # Return the app instance
    return app

