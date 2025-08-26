class UserRegisterDto:
    def __init__(self, name: str, age: int, email: str, phone: str):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

class UserFilterDto:
    def __init__(self, id_user: str):
        self.id_user = id_user

class UserLoginDto:
    def __init__(self, email: str):
        self.email = email
     
class UserUpdateDto:
    def __init__(self, id_user: str, name: str, age: int, email: str, phone: str):
        self.id_user = id_user
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone    

class UserResponseDto:
    def __init__(self, id_user: str, name: str, age: int, email: str, phone: str):
        self.id_user = id_user 
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def model_dump(self):
        return {
            "id_user": self.id_user,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone
        }
