
from api.config import session
from api.repository import UserRepository
from api.dto import (
    UserRegisterDto, # Registra novo usuário
    UserFilterDto, # Filtra usuário pelo ID usuário
    UserResponseDto, # Resposta do Usuário
    UserUpdateDto, # Atualizar as informações do Usuário
    UserLoginDto # Login do usuário
)
from uuid import uuid4

class UserService:
    def __init__(self):
        self.__user_repository = UserRepository(session=session)

    def add_user(self, user_register_dto: UserRegisterDto) -> UserResponseDto:
        user = self.__user_repository.add_user(
            name=user_register_dto.name,
            age=user_register_dto.age,
            email=user_register_dto.email,
            phone=user_register_dto.phone
        )
      
        user_response_dto = UserResponseDto(
            id_user=user.id_user,
            name=user.name,
            age=user.age,
            email=user.email,
            phone=user.phone
        )
        return user_response_dto
    
    def delete_user(self, user_filter_dto: UserFilterDto) -> None:
        return self.__user_repository.delete_user(user_filter_dto.id_user)
    
    def login_user(self, user_login_dto: UserLoginDto) -> UserResponseDto:
        user = self.__user_repository.login_user(email=user_login_dto.email)
        user_response_dto = UserResponseDto(
            id_user=user.id_user,
            name=user.name,
            age=user.age,
            email=user.email,
            phone=user.phone
        )
        return user_response_dto

    def update_user(self, user_update_dto: UserUpdateDto) -> UserResponseDto:
        user = self.__user_repository.update_user(
            id_user=user_update_dto.id_user,
            name=user_update_dto.name,
            age=user_update_dto.age,
            email=user_update_dto.email,
            phone=user_update_dto.phone
        )
        user_response_dto = UserResponseDto(
            id_user=user.id_user,
            name=user.name,
            age=user.age,
            email=user.email,
            phone=user.phone
        )
        return user_response_dto
    
    def select_user(self, user_filter_dto: UserFilterDto) -> UserResponseDto:
        user = self.__user_repository.select_user(
            id_user=user_filter_dto.id_user
        )
        user_response_dto = UserResponseDto(
            id_user=user.id_user,
            name=user.name,
            age=user.age,
            email=user.email,
            phone=user.phone
        )
        return user_response_dto