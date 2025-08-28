from pydantic import BaseModel, field_validator, field_serializer
from re import match
from uuid import UUID
from api.exceptions import UnprocessableEntity, InvalidFields

class UserRegisterDto(BaseModel):
    
    name: str
    email: str
    age: int
    phone: str

    @field_validator("email", mode="before")
    def validate_email(email):
        if  email == "":
            raise UnprocessableEntity("O email não pode ser vazio. Forneça um email válido.")
        if not match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            raise UnprocessableEntity("O e-mail informado é inválido.") 
        return email
    
    @field_validator("phone", mode="before")
    def validate_phone(phone: str) -> str:
       
        phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        if len(phone) < 11:
            raise UnprocessableEntity("O número deve conter no mínimo 11 dígitos o telefone.")
        if not phone.isnumeric():
            raise UnprocessableEntity("O número de celular devem ser números como (XX) 9XXXX-XXXX.")
        
        return phone

    @field_validator("name", "email", "age", "phone", mode="before")
    def validate_field(field) -> str | int:
        if field is None:
            raise InvalidFields("Os campos name, email, phone, age são obrigatórios.")
        return field
    
    @field_validator("name", mode="before")
    def validate_name(name: str) -> str:
        if name == "":
            raise UnprocessableEntity("O name não pode ser uma valor vazio ''.")
        return name

class UserFilterDto(BaseModel):

    id_user: str

    @field_validator("id_user", mode="before")
    def validate_id_user(id_user) -> str:
        if id_user is None:
            raise InvalidFields(f"Não foi fornecido o campo obrigatório - 'id_user'")
        try:
            UUID(str(id_user)) 
        except ValueError:
            raise UnprocessableEntity("O campo 'id_user' deve conter um UUID válido.")
        return id_user

class UserLoginDto(BaseModel):
    
    email: str

    @field_validator("email", mode="before")
    def validate_email(email):
        if  email == "":
            raise UnprocessableEntity("O email não pode ser vazio. Forneça um email válido.")
        if not match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            raise UnprocessableEntity("O e-mail informado é inválido.") 
        return email
    
     
class UserUpdateDto(BaseModel):

    id_user: str
    name: str
    email: str
    age: int
    phone: str

    @field_validator("id_user", mode="before")
    def validate_id_user(id_user) -> str:
        if id_user is None:
            raise InvalidFields(f"Não foi fornecido o campo obrigatório - 'id_user'")
        try:
            UUID(str(id_user)) 
        except ValueError:
            raise UnprocessableEntity("O campo 'id_user' deve conter um UUID válido.")
        return id_user

    @field_validator("email", mode="before")
    def validate_email(email):
        if  email == "":
            raise UnprocessableEntity("O email não pode ser vazio. Forneça um email válido.")
        if not match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            raise UnprocessableEntity("O e-mail informado é inválido.") 
        return email
    
    @field_validator("phone", mode="before")
    def validate_phone(phone: str) -> str:
       
        phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        if len(phone) < 11:
            raise UnprocessableEntity("O número deve conter no mínimo 11 dígitos o telefone.")
        if not phone.isnumeric():
            raise UnprocessableEntity("O número de celular devem ser números como (XX) 9XXXX-XXXX.")
        
        return phone

    @field_validator("name", "email", "age", "phone", mode="before")
    def validate_field(field) -> str | int:
        if field is None:
            raise InvalidFields("Os campos name, email, phone, age são obrigatórios.")
        return field
    
    @field_validator("name", mode="before")
    def validate_name(name: str) -> str:
        if name == "":
            raise UnprocessableEntity("O name não pode ser uma valor vazio ''.")
        return name  

class UserResponseDto(BaseModel):
    
    id_user: str
    name: str
    age: int
    email: str
    phone: str

    @field_serializer("phone", mode="plain")
    def serializer_phone(phone: str) -> str:
        return f"({phone[0:2]}) {phone[2:7]}-{phone[7:11]}"
    