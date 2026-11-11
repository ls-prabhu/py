class Error(Exception):
    """Base class for other exceptions"""
    pass

class PasswordTooShortError(Error):
    """Raised when the input password is too short"""
    pass

class PasswordTooLongError(Error):
    """Raised when the input password is too long"""
    pass


try:
    password = input("Enter a password: ")
    if len(password) < 6:
        raise PasswordTooShortError("Password is too short")
    elif len(password) > 12:
        raise PasswordTooLongError("Password is too long")
    else:
        print("Password is valid.")

        
except PasswordTooShortError as e:
    print(e)

except PasswordTooLongError as e:
    print(e)