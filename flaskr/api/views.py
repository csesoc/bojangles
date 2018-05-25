from flask import abort, jsonify, current_app
import json
from . import app


"""
Return json for all courses under <spec> specialisation
in <sem> semester (X1|S1|S2)
"""
@app.route('/specialisation/<spec>/<sem>')
def specialisation(spec, sem):
    sem = sem.upper()  # accept lower case request

    db_file = "%s/%s" % (current_app.root_path, current_app.config['CLASSUTIL_PATH'])
    db = json.load(open(db_file, 'r'))

    try:
        # todo: hesitant: Optimize this if scalability is required
        #       As it stands there are around 354 entries in the list, which we are searching through the entirety of
        #       as 354 is small, this is not really an issue, but we could easily optimize it by quitting as soon as
        #       we find a match, or we could just use a binary search (as the list is sorted by specialisation
        #       alphabetically)

        # We return next as the format guarantees there will only be one specialisation per session
        return jsonify(next(
            (x for x in db if x['specialisation'] == spec and x['session'] == sem)
        ))
    except StopIteration:
        # In the case of a empty return from filter, either the specialisation or session is invalid
        # (as there most be a object even if it has no courses)
        abort(400)
