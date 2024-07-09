# Define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

# Start of Program
# You need to guess this number
number = 10

# User guesses a number until he/she gets it right
while True:
    try:
        guess = int(input("Enter a number: "))
        if guess == number:
            print("Congratulations! You guessed it correctly.")
            break
        elif guess < number:
            raise ValueTooSmallError
        elif guess > number:
            raise ValueTooLargeError
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")



