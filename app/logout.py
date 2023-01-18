from flask import redirect, session
from flask_restful import Resource


class Logout(Resource):
    def get(self):
        if session:
            session.pop('username', None)
            return redirect('/')
        else:
            return "Not allowed", 400
