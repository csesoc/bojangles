from flask import abort, jsonify
import re
import json
from . import app


"""
Return json for all courses under <spec> specialisation
in <sem> semester (X1|S1|S2)
"""
@app.route('/specialisation/<spec>/<sem>')
def scraper(spec, sem):
    sem = sem.upper() # accept lower case request
    db = None
    with open(app.root_path + '/specialisation/db.json', 'r') as f:
        db = json.loads(f.read())
    
    try:
        return jsonify(
                [
                    i for i in db 
                    if i['specialisation']==spec and i['session']==sem
                ][0]
                )
    except:
        abort(400)

    """
    for i in db:
        if i['specialisation'] == spec and i['session'] == sem:
            return jsonify(i)
    abort(400)
    """
