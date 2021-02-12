from flask import Flask, jsonify, make_response, Response, request
import json



#rota com parametro livre
app = Flask(__name__)
@app.route("/exemplo/<id>" )
def hello(id):
    return "Hello Word, %s" %(id)

#rota com parametro int

@app.route("/exemploint/<int:id>" )
def helloint(id):
    return "Hello Word, %s" %(id)

@app.route("/jsonify")
def opt_json():
    retorno = {
    "message": "Respostas usando jsonify",
    "teste":"teste"
    }
    return jsonify(retorno)
@app.route("/make_response")
def opt_make_response():
    headers = { "content-type": "application/json"}
    retorno = {"message": "Respostas usando make_response"}
    return make_response(json.dumps(retorno), 201, headers)

@app.route("/response")
def opt_response():
    retorno = {"message": "Respostas usando response"}
    return Response(json.dumps(retorno), 201, content_type= "application/json")

@app.route("/request", methods=["POST"])
def corpoRequisicao():
    # data = request.form
    # data = request.args
    # data = request.values
    # data = request.cookies
    retorno = request.get_json()
    return Response(json.dumps(retorno),200, content_type= "application/json")


def opt_response():
    retorno = {"message": "Respostas usando response"}
    return Response(json.dumps(retorno), 201, content_type= "application/json")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5002)

