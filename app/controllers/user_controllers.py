
from app.models.users import User
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'app/static/uploads/profile_photo'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class UserController:
    @staticmethod
    def authenticate_user(email, password):
        return User.login_user(email, password)

    @staticmethod
    def create_user(email, password):
        return User.create_user(email, password)

    @staticmethod
    def complete_user_profile(user_id,first_name, last_name, doc_number, foto, mobile_number):
        try:
            image_path = None
            if foto:
                filename = secure_filename(foto.filename)
                image_path = os.path.join(UPLOAD_FOLDER, filename)
                foto.save(image_path)

            profile = User.complete_user(user_id,first_name, last_name, doc_number,image_path, mobile_number)

            if profile:
                return {"status": "sucesso", "mensagem": "Profile criado com sucesso!"}
            return  {"status": "erro", "mensagem": "Erro ao completar cadastro!"}

        except Exception as e:
            print(f'Erro: {e}')
        return False