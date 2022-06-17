from flask import ( Blueprint, request )
from . import models

# Create the Blueprint instance - Blueprint does our endpoint routing so this will be http://127.0.0.1:5000/reptiles

bp = Blueprint('reptiles', __name__, url_prefix="/reptiles") 

# pets = json.load(open('pets.json')) # Assign pets.json to a variable named pets

@bp.route('/', methods=['GET', 'POST'])
def index():
    # POST Route to add new reptile
    
    if request.method == 'POST':
        common_name = request.form['common_name'] # Grab common name
        scientific_name = request.form['scientific_name'] # Grab scientific name
        conservation_status = request.form['conservation_status'] # Grab conservation status
        native_habitat = request.form['native_habitat'] # Grab native habitat
        fun_fact = request.form['fun_fact'] # Grab fun fact
    
        new_reptile = models.Reptiles(common_name=common_name, scientific_name=scientific_name, conservation_status=conservation_status, native_habitat=native_habitat, fun_fact=fun_fact) # Call on Reptiles class in models.py thru new_reptile variable
        models.db.session.add(new_reptile) # Add new reptile to our database
        models.db.session.commit()

        return 'Added a new reptile!'
    
    # GET Route to show all reptiles
    
    results = models.Reptiles.query.all()

    rep_dict = {
        'all_reptiles': []
    }

    for result in results:
        rep_dict['all_reptiles'].append({
            'id': result.id,
            'common_name': result.common_name,
            'scientific_name': result.scientific_name,
            'conservation_status': result.conservation_status,
            'native_habitat': result.native_habitat,
            'fun_fact': result.fun_fact
        })
    
    return rep_dict
    

@bp.route('/<int:id>')
def show(id):
  reptiles = models.Reptiles.query.filter_by(id=id).first()
  rep_dict = {
    'common_name': reptiles.common_name,
    'scientific_name': reptiles.scientific_name,
    'conservation_status': reptiles.conservation_status,
    'native_habitat': reptiles.native_habitat,
    'fun_fact': reptiles.fun_fact
  }

  return rep_dict


