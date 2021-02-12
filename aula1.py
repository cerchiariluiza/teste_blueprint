import requests


#JSON EM DOCS
#pega o indice
# requisicao = requests.get("http://localhost:9200/adega5/_search")
# print(requisicao)
#converte em json
# json_to_dict = requisicao.json()
#chama os dados
# print(json_to_dict["hits"]["hits"][0]["_index"])


data = {
        "nome":"joao",
        "sobrenome":"hummel"
}

# requisicao = requests.post("http://httpbin.org/post", json=data)
# json_to_dict = requisicao.json()
# print(json_to_dict)

requisicao = requests.patch("http://httpbin.org/patch", json=data)
json_to_dict = requisicao.json()
print(json_to_dict["json"])
