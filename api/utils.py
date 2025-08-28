from flask import jsonify

def send_response_erro(erro: str, message: str, status_http: int):
        return jsonify(
            {
                "type": message,
                "erro": erro,
            }
        ), status_http

