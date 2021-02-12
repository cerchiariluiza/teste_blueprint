from flask import Blueprint
from flask import Flask

import json

grupos_routes = Blueprint("grupos", __name__, url_prefix="/grupos")


@grupos_routes.route("")
def getGrupos():
    return "Lista de grupos"