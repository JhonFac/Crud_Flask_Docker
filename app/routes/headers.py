from functools import wraps

from flask import abort, request

from app.utils.response import error_response, success_response

headers_required = ["X-Channel", "X-CustIdentNum", "X-CustIdentType", "X-IPAddr", "X-Name", "X-RqUID"]


def require_headers(required_headers):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            headers_missing = list(filter(lambda x: x not in request.headers, required_headers))
            if headers_missing:
                return error_response(f'Header(s) {",".join(headers_missing)} is(are) required', 400)
            return view_func(*args, **kwargs)

        return wrapper

    return decorator
