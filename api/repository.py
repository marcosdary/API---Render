from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from api.model import User
from api.exceptions import EntityValidationError, NotFoundError, DuplicateReviewError

class UserRepository:
    def __init__(self, session: Session):
        self.__session = session

    def add_user(self, name: str, age: int, email: str, phone: str) -> User:
        try:
            email_exists = self.__session.query(User).filter(User.email == email).first()

            if not email_exists is None:
                raise DuplicateReviewError("E-mail já cadastrado na base de dados.")
            
            phone_exists = self.__session.query(User).filter(User.phone == phone).first()

            if not phone_exists is None:
                raise DuplicateReviewError("Número de celular já cadastrado na base de dados.")

            user = User()
            user.name = name
            user.age = age
            user.email = email
            user.phone = phone

            self.__session.add(user)
            self.__session.commit()
            return user
        
        except IntegrityError as e:
            if self.__session.is_active:
                self.__session.rollback()
            raise EntityValidationError(f"Ocorreu um erro no momento do salvamento do usuário: {str(e)}")

        except Exception as e:
            if self.__session.is_active:
                self.__session.rollback()
            raise e
        
    def login_user(self, email: str) -> User:
        
        user = self.__session.query(User).filter(User.email == email).first()

        if user is None:
            raise NotFoundError("E-mail não encontrado. Tente novamente.")

        return user
    
    def update_user(self, id_user: str, name: str, age: int, email: str, phone: str) -> User:
        try:
            
            user = self.__session.query(User).filter(User.id_user == id_user).first()

            if user is None:
                raise NotFoundError("Usuário não encontrado. Tente novamente.")
            
            email_exists = self.__session.query(User).filter(User.email == email).first()

            if email_exists is not None and user.id_user != email_exists.id_user:
                raise DuplicateReviewError("E-mail já cadastrado na base de dados.")
            
            phone_exists = self.__session.query(User).filter(User.phone == phone).first()

            if phone_exists is not None and user.id_user != phone_exists.id_user:
                raise DuplicateReviewError("Número de celular já cadastrado na base de dados.")
            
            user.name = name
            user.age = age
            user.email = email
            user.phone = phone

            self.__session.commit()

            return user
        
        except IntegrityError as e:
            if self.__session.is_active:
                self.__session.rollback()
            raise EntityValidationError(f"Ocorreu um erro no momento do atualizar as informações do usuário: {str(e)}")

        except Exception as e:
            if self.__session.is_active:
                self.__session.rollback()
            raise e
    
    def select_user(self, id_user: str) -> User:

        user = self.__session.query(User).filter(User.id_user == id_user).first()

        if user is None:
            raise NotFoundError("Usuário não encontrado. Tente novamente.")

        return user
    
    def delete_user(self, id_user: str) -> None:
        try:
            user = self.__session.query(User).filter(User.id_user == id_user).first()
            if user is None:
                raise NotFoundError("Usuário não encontrado. Tente novamente.")
            self.__session.delete(user)
            self.__session.commit()
            return 

        except IntegrityError as e:
            if self.__session.is_active:
                self.__session.rollback()
            raise EntityValidationError(f"Ocorreu um erro no momento de deletar o usuário: {str(e)}")
        
        except Exception as e:
            if self.__session.is_active:
                self.__session.rollback()
            raise e