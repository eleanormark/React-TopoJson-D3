from flask import render_template, Blueprint, current_app, jsonify, abort, request
from .models import Specialties, Physicians

endpoints = Blueprint('endpoints', __name__)

SIZE_ERROR = "'size' must be a positive int"


def response(data, status=200):
    """Return a Flask-formatted response."""

    return jsonify(data), status, {'Content-Type': 'application/json'}


@endpoints.route('/')
def index():
    return render_template("index.html")

@endpoints.route('/physicians')
def show_physicians():
    """Return a list of specialties in descending order of count."""

    size = request.args.get("size")

    try:
        size = _none_or_int(size)

        if size is not None and size <= 0:
            return response({"error": SIZE_ERROR}, status=400)

    except ValueError:
        return response({"error": SIZE_ERROR}, status=400)

    query = (
        current_app.session.query(Physicians)
        .order_by(Physicians.state.asc())
    )

    physicians = [{'state':row.state, 'count':row.count, 'specialty': row.specialty} for row in query]

    if size:
        physicians = physicians[:size]

    return response({
        'physicians': physicians
    })


@endpoints.route('/specialties')
def show_specialties():
    """Return a list of specialties in descending order of count."""

    size = request.args.get("size")

    try:
        size = _none_or_int(size)

        if size is not None and size <= 0:
            return response({"error": SIZE_ERROR}, status=400)

    except ValueError:
        return response({"error": SIZE_ERROR}, status=400)

    query = (
        current_app.session.query(Specialties)
        .order_by(Specialties.count.desc())
    )

    specialties = [{'specialty':row.specialty, 'count':row.count} for row in query]

    if size:
        specialties = specialties[:size]

    return response({
        'specialties': specialties
    })


def _none_or_int(var):

    if var is not None:
        var = int(var)

    return var
