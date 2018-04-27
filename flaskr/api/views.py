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

    db_file = app.root_path + '/specialisation/db.json'
    # Try to read the json from the db file, fail gracefully and log an error
    try:
        db = json.load(open(db_file, 'r'))
    except (json.JSONDecodeError, OSError) as err:
        db_file.close()
        current_app.logger.error(
            'API endpoint [/api/specialisation/%s/%s] failed when loading json from:\n%s\n%s',
            spec, sem, db_file, err
        )
        abort(500)

    try:
        # todo: hesitant: Optimize this if scalability is required
        #       As it stands there are around 354 entries in the list, which we are searching through the entirety of
        #       as 354 is small, this is not really an issue, but we could easily optimize it by quitting as soon as
        #       we find a match, or we could just use a binary search (as the list is sorted by specialisation
        #       alphabetically)

        # We return next as the format guarantees there will only be one specialisation per session
        return jsonify(next(
            filter(lambda rec: rec['specialisation'] == spec and rec['session'] == sem, db)
        ))
    except StopIteration:
        # In the case of a empty return from filter, either the specialisation or session is invalid
        # (as there most be a object even if it has no courses)
        abort(400)
