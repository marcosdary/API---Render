from api.config import PATH_DATAS
from json import load, dump
from flask import jsonify

def read_users() -> list:
    with open(PATH_DATAS, "r", encoding="utf-8") as file:
        return load(file)
    
def write_users(info: list):
    with open(PATH_DATAS, "w", encoding="utf-8") as file:
        dump(info, file, ensure_ascii=True, indent=4)

def send_response_erro(erro: str, message: str, status_http: int):
        return jsonify(
            {
                "type": message,
                "erro": erro,
            }
        ), status_http

