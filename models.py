from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Create a variable named 'db' to our instance of SQLAlchemy class

# Create Class/Model for use with Migrations
# 
# Sample Reptile Data for creating our model below
# 
# {
#     'common_name': 'Ball python',
#     'scientific_name': 'Python regius',
#     'conservation_status': 'Near threatened',
#     'native_habitat': 'Forest, savanna, shrubland, grassland',
#     'fun_fact': 'Ball pythons received their common name
#         from their behavior of curling up into a ball when threatened.'
# }


class Reptiles(db.Model):
    __tablename__= 'reptiles' # Create the table name

    id = db.Column(db.Integer, primary_key=True) # Primary key column for the table
    common_name = db.Column(db.String(250)) # Type is String with a character limit of 250
    scientific_name = db.Column(db.String(100)) # Type is String with a character limit of 100
    conservation_status = db.Column(db.String(100)) # Type is String with a character limit of 100
    native_habitat = db.Column(db.String(250)) # Type is String with a character limit of 250
    fun_fact = db.Column(db.Text)