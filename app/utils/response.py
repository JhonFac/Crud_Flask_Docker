import json
from datetime import datetime

from flask import Flask, abort, jsonify

now = datetime.now()
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S.%f")


def success_response(data=None):
    """
    Returns a success response with optional data.
    """
    response = {"success": True}
    if data:
        response["data"] = data
    return jsonify(response)


def error_response(message, status_code):
    """
    Returns an error response with a message and status code.
    """
    response = {"StatusCode": status_code, "Description": message, "TimeStamp": formatted_date}
    return jsonify(response), status_code


def register_error_handlers(app):
    @app.errorhandler(500)
    def internal_server_error(error):
        response = {"StatusCode": "500", "Description": "Processing Error", "TimeStamp": formatted_date}
        return jsonify(response), 500
