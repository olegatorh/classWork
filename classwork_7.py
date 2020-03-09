try:
    custom_number = int(input("Please enter integer number: "))
    if custom_number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
except ValueError:
    print("Sorry, the number is not valid")
except TypeError:
    print("The type you entered is wrong!")


class NegativeAge(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    age = int(input("Please enter your age: "))
    if age < 0:
        raise NegativeAge("Age can't be negative!")
    if age % 2 == 0:
        print("The age number is even")
    elif age % 2 != 0:
        print("The age number is odd")
except TypeError:
    print("The type you entered is wrong!")
except ValueError:
    print("Wrong value!")


try:
    x, y = eval(input("Please enter 2 numbers separated by come: "))

    z = x / y
    print(z)

except ZeroDivisionError:
    print("You can't divide by zero!!")
except SyntaxError:
    print("Coma is missing. Please enter 2 numbers separated by coma!")
# 65866hgjh75785
except:
    print("Wrong input")
else:
    print("No exceptions. You entered valid numbers")
finally:
    print("Good bye!")


week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


class OutOfIndexRange(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    day = int(input("Please enter the number: "))
    if day <= 0 or day > 7:
        raise OutOfIndexRange("No week day corresponding to the number!")
    else:
        print(week[day])

except OutOfIndexRange as o:
    print(f"Custom exception:{o.data}")
except SyntaxError:
    print("Please enter valid number!")
except ValueError:
    print("Please enter correct number!")
finally:
    print("End of the program!")