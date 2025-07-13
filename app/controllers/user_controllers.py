
from app.models.users import User
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'app/static/uploads/profile_photo'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class UserController:
    @staticmethod
    def create_user(email, password):
        return User.create_user(email, password)

    @staticmethod
    def complete_user_profile(user_id,first_name, last_name, doc_number, foto, mobile_number):
        doc_equals = User.get_doc_register(doc_number)
        if doc_equals:
            return False, "CPF Já registrado.", "danger", "user.complete_register"

        foto_user = None
        if foto:
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(UPLOAD_FOLDER, filename))
            foto_user = filename

        profile = User.complete_user(user_id,first_name, last_name, doc_number,foto_user, mobile_number)

        if profile:
            return True, "Profile criado com sucesso!", "success", "user.dashboard"
        return  False, "Erro ao completar cadastro!", "danger", "user.complete_register"

    @staticmethod
    def verify_token(user_id,token):
      return User.check_token(user_id,token)

    @staticmethod
    def token_is_verified(user_id):
        return User.token_verified(user_id)

    @staticmethod
    def login_user_and_redirect(email,password):
        user = User.login_user(email,password)
        if not user:
            return None, 'Usuario ou senha incorreto!','danger','user.dashboard'
        if User.token_verified(user.id):
                return user, 'Login com sucesso!', 'success', 'user.dashboard'
        else:
                return user,'Token de verificação necessário','danger', 'user.verify_token'

    @staticmethod
    def view_profile(user_id):
        user = User.get_profile_user(user_id)
        if user:
            return user , 'Usuário com perfil cadastrado!','success','user.view_profile'
        return user , 'Usuário sem perfil cadastrado!', 'danger', 'user.complete_register'

    @staticmethod
    def update_password(user_id,old_password, new_password):
        user = User.update_password(user_id,old_password, new_password)
        if user:
            return user, "Senha alterada com sucesso!", "success", "user.dashboard"
        return user, "Senha invalida, tente novamente!", "danger", "user.update_password"

