from flask import abort, request

from app.utils.response import error_response, success_response

headers_required = ["X-Channel", "X-CustIdentNum", "X-CustIdentType", "X-IPAddr", "X-Name", "X-RqUID"]


def require_headers(required_headers):
    def decorator(view_func):
        def wrapper(*args, **kwargs):
            for header in required_headers:
                if header not in request.headers:
                    return error_response(f"Header {header} is required", 400)
            return view_func(*args, **kwargs)

        return wrapper

    return decorator
