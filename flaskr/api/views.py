from flask import jsonify, current_app, request
import json
from . import app
from .schedule import generate_schedule

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



"""
Returns all timeslots for given courses and generated
schedule(s)
Endpoint: /api/schedule
Request Payload(JSON):
    {
        'courses': ['COMP1511', 'COMP1521'],
        'preference': ['pref-opt1', 'pref-opt2']
    }
"""
@app.route('/schedule', methods=['POST'])
def schedule():
    courses = request.json['courses']
    db_file = "%s/%s" % (current_app.root_path, current_app.config['CLASSUTIL_PATH'])
    db = json.load(open(db_file, 'r'))
    # TODO: optimise runtime / pass in preference options
    return jsonify(generate_schedule(courses, db['S2']))
