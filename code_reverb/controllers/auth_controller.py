from flask import request, g, session, redirect, render_template, url_for, make_response
import flask_restx
from functools import wraps
from flask_restx import Namespace
from marshmallow import ValidationError

api = Namespace("auth", description="auth related operations")


def load_logged_in_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        g.user = get_user_by_id(user_id) if user_id else None
        return func(*args, **kwargs)

    return wrapper


class Resource(flask_restx.Resource):
    method_decorators = [load_logged_in_user]
