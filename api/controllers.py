from flask import request, jsonify
from api.utils import send_response_erro
from api.dto import (
    UserRegisterDto,
    UserUpdateDto,
    UserFilterDto,
    UserLoginDto
)
from api.service import UserService

user_service = UserService()

class UserController:
    @staticmethod
    def add_user():
        try:
            info_user: dict = request.json
            user_register_dto = UserRegisterDto(
                name=info_user["name"],
                age=info_user["age"],
                email=info_user["email"],
                phone=info_user["phone"]
            )
            user_response_dto = user_service.add_user(user_register_dto)
            return jsonify(user_response_dto.model_dump()), 201
        except ValueError as e:
            return send_response_erro(type(e).__name__, str(e), 401)
        except Exception as e:
            return send_response_erro(type(e).__name__, str(e), 500)
        
    @staticmethod
    def login_user(): 
        try:
            info_user: dict = request.args
            user_login_dto = UserLoginDto(
                email=info_user["email"]
            )
            user_response_dto = user_service.login_user(user_login_dto)
            return jsonify(user_response_dto.model_dump()), 200
        except ValueError as e:
            return send_response_erro(type(e).__name__, str(e), 401)
        except Exception as e:
            return send_response_erro(type(e).__name__, str(e), 500)

    @staticmethod
    def select_user(id_user: str):
        try:
            user_filter_dto = UserFilterDto(
                id_user=id_user
            )
            user_response_dto = user_service.select_user(user_filter_dto)
            return jsonify(user_response_dto.model_dump()), 200
        except ValueError as e:
            return send_response_erro(type(e).__name__, str(e), 401)
        except Exception as e:
            return send_response_erro(type(e).__name__, str(e), 500)
       
    
    @staticmethod
    def update_user(id_user: str):
        try:
            info_user: dict = request.json
            user_update_dto = UserUpdateDto(
                id_user=id_user,
                name=info_user["name"],
                age=info_user["age"],
                email=info_user["email"],
                phone=info_user["phone"]
            )
            user_response_dto = user_service.update_user(user_update_dto)
            return jsonify(user_response_dto.model_dump()), 200
        except ValueError as e:
            return send_response_erro(type(e).__name__, str(e), 401)
        except Exception as e:
            return send_response_erro(type(e).__name__, str(e), 500)

    @staticmethod
    def delete_user(id_user: str):
        try:
            user_filter_dto = UserFilterDto(
                id_user=id_user
            )
            user_service.delete_user(user_filter_dto)
            return jsonify({"message": "Sucesso em apagar o usuário"}), 200
        except ValueError as e:
            return send_response_erro(type(e).__name__, str(e), 401)
        except Exception as e:
            return send_response_erro(type(e).__name__, str(e), 500)
    
