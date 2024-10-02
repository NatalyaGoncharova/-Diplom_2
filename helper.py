class UserData:
    @staticmethod
    def get_user_registration_data(email, password, name):
        return {"email": email, "password": password, "name": name}

    @staticmethod
    def get_user_login_data(email, password):
        return {"email": email, "password": password}

    @staticmethod
    def get_user_logout_data(refresh_token):
        return {"token": refresh_token}




