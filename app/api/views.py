# api/views.py

from flask import Flask, Blueprint, json, jsonify
from flask_sqlalchemy import *

from app.models import PostHome

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/api/homes', methods=['GET'])
def api_get_home_posts():
	posts = PostHome.query.all()
	return jsonify({'homes': [post.serialize() for post in posts]})