def integer_check(question):
    """
    Check the input field.
    Return the integer, if all characters in the string are digits,
    and there is at least one character.
    Example:
        a = integer_check('Please write an integer: ')
    """
    x = False
    while x != True:
        i = input(question)
        x = str.isdigit(i)
    i = int(i)
    return i

def name_check(question):
    """
    Check the input field.
    Return the string if all character is string.
    Include 'space' character check.
    The entered string can be arbitrary.
    Example:
        a = name_check('What's your real name: ')
    """
    while True:
        try:
            s = input(question)
            f = float(s)
        except ValueError:
            break
    return s

def string_check(question):
    """
    Check the input field.
    Return the string, if all characters in the string are alphabetic,
    and there is at least one character.
    The 'space' character is don't accept.
    Therefore, only one word can be the string you type.
    Example:
        a = string_check('What's your nickname: ')
    """
    y = False
    while y != True:
        s = input(question)
        y = str.isalpha(s)
    return s

def range_check(question,a,b):
    """
    Checks your choice between two numbers.
    Returns the selected number.
    Example:
        a = range_check('Please choose in the range: ',1,10)
    """
    y = 0
    while y != 1:
        try:
            i = int(input(question))
            if i in range(a,b+1):
               y = 1
               pass
            else:
               print("The number is in out of range!")
               y = 0
        except ValueError:
            print ("This is not a number, or not an integer value!")
            y = 0
    return i

def float_check(question):
    """
    Check the input field.
    Returns only 'float' number.
    Example:
        a = float_check('Please write an 'float' number: ')
    """
    y = False
    while y != True:
        f = input(question)
        if len(f) == 0:
            print("Please write something!")
            y = False
        else:
            pass
            try:
                int(f)
                y = False
            except:
                try:
                    float(f)
                    y = True
                except:
                    pass

    return f