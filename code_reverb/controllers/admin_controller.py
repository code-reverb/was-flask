from flask import g
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect, url_for
from flask import jsonify
from flask_restx import Namespace
# call func
import json
from code_reverb.utils.common import execute_command
# <tmp>
# - 로그인 중인 사용자 아이디 점검 기능 등,
# - auth/user controller 작성 시 해당 파일로 이관
from flask_restx import Resource


# 관리자 페이지용 controller
api = Namespace("admin", description="admin related operations")


# 관리자 메인 페이지: 관리자용 대시보드 <우선도: 1>
# - 이상이 있는 컨테이너 목록 표시
# - 이상이 있는 데이터베이스 클러스터, 샤드, 인덱스 목록 표시
# - 발견된 컨테이너 취약점 목록 표시
# - 최근 댓글이 달린 블로그 글 목록 표시
# - 최근 올라온 질의응답, 건의&문의 게시판 제목/작성자/일자 목록 표시
@api.route("/")
class CodereverbAdmin(Resource):
    @api.doc("project admin page")
    def get(self):
        return make_response(
            render_template(
                "admin/index.html"
            )
        )


# 관리자용 컨테이너 관리 페이지
# - 전체 컨테이너 목록 표시
# - 페이지네이션
@api.route("/containers")
class ContainerAdmin(Resource):
    @api.doc("project container page")
    def get(self):
        return make_response(
            render_template(
                "admin/index.html"
            )
        )


"""
# <container>
# - 전체 목록 표시
@api.route("/containers/list")
class ContainerList(Resource):
    @api.doc("container list")
    def get(self):
        # get param
        size = request.args.get('size', '*')

        # var init
        result_data = list()

        # container ps raw data
        command = "docker ps -a --format='{{json .}}'"
        raw_data = execute_command(command)

        # container ret process
        datas = raw_data.split("\n")
        for index, data in enumerate(datas):
            # - option chk
            if size != "*" and index == size:
                break

            # - raw data to json
            data = data.replace("\\\"", "")
            try:
                container_data = json.loads(data)
            except json.decoder.JSONDecodeError:
                msg = "Error: docker ps 데이터 파싱에 실패했습니다."
                print(msg, data)
                result = {"result_code": -1, "data": msg}
                return make_response(jsonify(result))

            # pre-raw_data
            del container_data["Labels"]
            del container_data["Mounts"]
            del container_data["LocalVolumes"]
            if 'Up' in container_data['Status']:
                container_data['Type'] = 'run'
            else:
                container_data['Type'] = 'stop'

            result_data.append(container_data)
        result = {"result_code": 0, "data": result_data}
        return make_response(jsonify(result))


# - 컨테이너 상태/실행or중지/삭제
@api.route("/container/<string:container_id>")
class ContainerControl(Resource):
    @api.doc("container status check")
    def get(self):
        # 도커 컨테이너 실행
        command = f"docker ps -a -f id={container_id}" + " --format='{{json .}}'"
        raw_data = execute_command(command)
        data = raw_data.replace("\\\"", "")
        try:
            container_data = json.loads(data)
        except json.decoder.JSONDecodeError:
            msg = "Error: docker ps 데이터 파싱에 실패했습니다."
            print(msg, data)
            return {"result_code": -1, "data": msg}
        except Exception as e:
            msg = "Error: docker ps 데이터를 가져오지 못했습니다."
            print(msg, e, data)
            return {"result_code": -1, "data": msg}

        # 값 반환
        status = container_data["Status"]
        return {"result_code": 0, 'data': status}


    @api.doc("container start/stop")
    def post(self):
        # param
        # - start
        command = f"docker start {container_id}"
        raw_data = execute_command(command)
        result = {"result_code": 0, "data": raw_data}
        return make_response(jsonify(result))


    @api.doc("container remove")
    def delete(self):
        command = f'docker stop {container_id}'
        data = execute_command(command)
        return {"result_code": 0, 'data': data}
"""
