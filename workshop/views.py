from flask import Blueprint, jsonify

from workshop.models import Cat

api = Blueprint('api', __name__)


@api.route('/cats/')
def list_cats():
    cats = [{'name': c.name, 'country': c.country} for c in Cat.all()]
    return jsonify(cats)
