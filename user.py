
class User():
    def __init__(self, name, email, password):
        self.__name = name
        self.email = email
        self.__password = None

        self.__validate_password(password)
        self.__password = password

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if (isinstance(value , str)
            and value.strip()
            and not isinstance(value , bool)
            and "@" in value.strip()
            and "." in value.strip().split("@")[-1]):
            self.__email = value
        else:
            raise ValueError("the email in invalid!")
        
    def __validate_password(self, password):
        if (
            isinstance(password, str)
            and len(password) >= 8
        ):
            return True
        raise ValueError("Password must contain at least 8 characters.")

    def change_password(self,old_password, new_password):
        if  old_password == self.__password :
            self.__validate_password(new_password)
            self.__password = new_password
        else:
            raise ValueError ("password is invalid!")
        
    def get_info(self):

        info_user = {}
        info_user["name"] = self.__name
        info_user["email"] = self.email
        return info_user