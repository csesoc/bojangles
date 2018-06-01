from flask import jsonify, current_app
import json
from . import app

"""
Returns a list of courses running in a specific semester
Endpoint: /api/courses/(S1 | S2 | X1)
"""
@app.route('/courses/<sem>')
@app.route('/courses/<sem>/<course>')
def course(sem, course=None):
    db_file = "%s/%s" % (current_app.root_path, current_app.config['CLASSUTIL_PATH'])
    db = json.load(open(db_file, 'r'))

    try:
        courses = db[sem]
    except KeyError:
        return "Semester %s does not exist" % sem, 400

    if course is None:
        return jsonify([(code, data['description']) for code, data in courses.items()])
    else:
        try:
            return jsonify(courses[course])
        except KeyError:
            return "Course %s does not exist" % course, 400
