from flask import redirect, url_for, make_response
from flask_restx import Namespace
from code_reverb.controllers.auth_controller import Resource


api = Namespace("main", description="main related operations")


@api.route("/")
@api.route("/index")
class Index(Resource):
    @api.doc("show main page")
    def get(self):
        return redirect(url_for("api.admin_codereverb_admin"))
