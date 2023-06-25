from flask import request, Blueprint, current_app
import http
import time
import os
import json

mock_blueprint = Blueprint("mock_blueprint", __name__)

@mock_blueprint.route("/")
def index():
    return "Hello World!"

@mock_blueprint.route("/resource")
def resource():
    data = request.args.get("data")
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, f'static/{data}')    
    
    try:
        with open(data_file, "r") as file:
            current_app.logger.info(f"Receive data from file {data}")
            return json.loads(file.read())
    except FileNotFoundError:
        current_app.logger.info(f"File {data} is not found, return empty response")
        return []

@mock_blueprint.route("/status")
def status():
    code = int(request.args.get("code"))
    current_app.logger.info(f"Receive http code {code}")
    try:
        response = current_app.response_class(
            response=f"{code} {http.HTTPStatus(code).name}",
            status=code,
            mimetype='application/json'
        )
    except ValueError as e:
        response = current_app.response_class(
            response=f"{e}",
            status=code,
            mimetype='application/json'
        )
    return response

@mock_blueprint.route("/delay")
def delay():
    ms = int(request.args.get("ms"))
    current_app.logger.info(f"Receive sleep time {ms} milliseconds")
    time.sleep(ms/1000)
    return f"Response with delay of {ms} milliseconds"

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)