from functools import wraps
from flask import session, redirect

def role_required(required_role):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if "role" not in session:
                return redirect("/login")

            if session["role"] != required_role:
                return redirect("/login")

            return func(*args, **kwargs)

        return wrapper

    return decorator