from utils import read_users, write_users
from dto import (
    UserRegisterDto, # Registra novo usuário
    UserFilterDto, # Filtra usuário pelo ID usuário
    UserResponseDto, # Resposta do Usuário
    UserUpdateDto, # Atualizar as informações do Usuário
    UserLoginDto # Login do usuário
)
from uuid import uuid4

class UserService:
    def __init__(self):
        self._write_user = write_users
        self._read_users = read_users()

    def add_user(self, user_register_dto: UserRegisterDto) -> UserResponseDto:
        users = self._read_users
        for user in users:
            if user["email"] == user_register_dto.email:
                raise ValueError("Já existe o e-mail cadastrado no sistema.")
            if user["phone"] == user_register_dto.phone:
                raise ValueError("Já existe o número de celular no sistema.")
        
        user_response_dto = UserResponseDto(
            id_user=str(uuid4()),
            name=user_register_dto.name,
            age=user_register_dto.age,
            email=user_register_dto.email,
            phone=user_register_dto.phone
        )
        users.append(user_response_dto.model_dump())
        self._write_user(users)
        return user_response_dto
    
    def delete_user(self, user_filter_dto: UserFilterDto) -> None:
        users = self._read_users
        for index, user in enumerate(users):
            if user["id_user"] == user_filter_dto.id_user:
                users.pop(index)
                self._write_user(users)
                return
            
        raise ValueError(f"Não foi possível encontrar o usuário com o ID {user_filter_dto.id_user}")
    
    
    def login_user(self, user_login_dto: UserLoginDto) -> UserResponseDto:
        users = self._read_users
        for user in users:
            if user["email"] == user_login_dto.email:
                user_response_dto = UserResponseDto(
                    id_user=user["id_user"],
                    name=user["name"],
                    age=user["age"],
                    email=user["email"],
                    phone=user["phone"]
                )
                return user_response_dto

    def update_user(self, user_update_dto: UserUpdateDto) -> UserResponseDto:
        users = self._read_users
        for user in users:
            if user["id_user"] == user_update_dto.id_user:
                user["name"] = user_update_dto.name
                user["age"] = user_update_dto.age
                user["email"] = user_update_dto.email
                user["phone"] = user_update_dto.phone
                self._write_user(users)

                user_response_dto = UserResponseDto(
                    id_user=user_update_dto.id_user,
                    name=user_update_dto.name,
                    age=user_update_dto.age,
                    email=user_update_dto.email,
                    phone=user_update_dto.phone
                )
                return user_response_dto
            
        raise ValueError(f"Não foi possível encontrar o usuário com o ID {user_update_dto.id_user}")
    
    def select_user(self, user_filter_dto: UserFilterDto) -> UserResponseDto:
        users = self._read_users
        for user in users:
            if user["id_user"] == user_filter_dto.id_user:

                user_response_dto = UserResponseDto(
                    id_user=user["id_user"],
                    name=user["name"],
                    age=user["age"],
                    email=user["email"],
                    phone=user["phone"]
                )
                return user_response_dto
            
        raise ValueError(f"Não foi possível encontrar o usuário com o ID {user_filter_dto.id_user}")