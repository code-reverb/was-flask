from flask import g
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect, url_for
from flask_restx import Namespace
# <tmp>
# - 로그인 중인 사용자 아이디 점검 기능 등,
# - auth/user controller 작성 시 해당 파일로 이관
from flask_restx import Resource


# 관리자 페이지용 controller
api = Namespace("admin", description="admin related operations")


@api.route("/")
class CodereverbAdmin(Resource):
    @api.doc("project admin page")
    def get(self):
        return make_response(
            render_template(
                "admin/index.html"
            )
        )
