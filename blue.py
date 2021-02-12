from flask import Flask, Response
from blueprint import grupos_routes
import json

app = Flask(__name__)
app.register_blueprint(grupos_routes)
from blue import blueprint
@app.route("/")
def index():
    retorno = {
        "app": "Sistema de mensagens",
        "version": 1.8
    }
    return Response(
        json.dumps(retorno), 
        200, 
        content_type="application/json")
        
if __name__ == "__main__":
    app.run(debug=True)