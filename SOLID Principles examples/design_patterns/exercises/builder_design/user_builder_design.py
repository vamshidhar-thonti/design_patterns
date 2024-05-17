from abc import ABC, abstractmethod

class User:
    def __init__(self) -> None:
        self._first_name = None
        self._last_name = None
        self._age = None
        self._phone_number = None
        self._address = None
        self._email_address = None

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    def get_address(self):
        return self._address

    def get_email_address(self):
        return self._email_address
    
class UserBuilder(ABC):
    def __init__(self) -> None:
        self.user = User()

    def get_user(self):
        return self.user.__dict__
    
    @abstractmethod
    def set_first_name(self, first_name):
        pass

    @abstractmethod
    def set_last_name(self, last_name):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def set_phone_number(self, phone_number):
        pass

    @abstractmethod
    def set_address(self, address):
        pass

    @abstractmethod
    def set_email_address(self, email_address):
        pass

class CustomUserBuilder(UserBuilder):
    def __init__(self) -> None:
        super().__init__()

    def set_first_name(self, first_name):
        self.user._first_name = first_name

    def set_last_name(self, last_name):
        self.user._last_name = last_name

    def set_age(self, age):
        self.user._age = age

    def set_phone_number(self, phone_number):
        self.user._phone_number = phone_number

    def set_address(self, address):
        self.user._address = address

    def set_email_address(self, email_address):
        self.user._email_address = email_address

class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self.builder = builder

    def create_new_user(self, user_data):
        self.builder.set_first_name(user_data['first_name'])
        self.builder.set_last_name(user_data['last_name'])
        self.builder.set_age(user_data.get('age', None))
        self.builder.set_phone_number(user_data.get('phone_number', None))
        self.builder.set_address(user_data.get('address', None))
        self.builder.set_email_address(user_data['email_address'])

def main():
    user_data = {
        'first_name': 'Vamshidhar',
        'last_name': 'Thonti',
        'age': 26,
        'email_address': 'vamshi@test.com'
    }

    custom_user_builder = CustomUserBuilder()
    user_director = UserDirector(custom_user_builder)
    user_director.create_new_user(user_data)
    current_user = user_director.builder.get_user()
    print(current_user)

if __name__ == '__main__':
    main()