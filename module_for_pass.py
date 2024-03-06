def get_user_number() -> int:
    """
    Function gets a 5-digits number
    :raises ValueError This exception is thrown when the user's number is not numeric
    :return: Getting user's 5-digits number
    """
    try:
        return int(input("Please enter a 5-digit number that is bigger than 11111, lower than 66666: "))
    except ValueError:
        raise ValueError("Your input is not a valid 5-digit number!")


def check_5_digits() -> int:
    '''
    Function checks if the number is 5-digits number
    if not the function asks user to input another input
    :return: 5-digits number
    '''
    n = get_user_number()
    while not (11110 < n < 66667):
        n = get_user_number()

    return n


def input_father() -> list:
    """
    Function doesn't get anything
    :return: a list with tree numbers, every number 5-digits
    """
    numbers_list = []
    for _ in range(3):
        try:
            input_number = check_5_digits()
            numbers_list.append(input_number)
        except ValueError as e:
            print("Error:", e)
    return numbers_list


def user_num_in_out_txt(list_of_nums) -> str:
    """
    Function gets list of number with length 3
    :list_of_nums: a 3-number list
    :return: string of three words without spaces
    """
    out_str = ""
    number_digits = len(list_of_nums)
    if (number_digits != 3):
        return "The list aren't correct something got wrong"
    else:
        for numbers in list_of_nums:
            out_str = out_str + transforms_num(numbers)[1:-1]
    return out_str


def transforms_num(number) -> str:
    """
    Function gets a number and looks for it in the text file
    :param number:number from the user after checking it
    :return: string of the value of number than in text file (\t****\n)
    """
    formed_list = []
    str_out = ""
    try:
        with open('diceware.txt', 'r') as f:
            formed_list = ([line for line in f if line.startswith(str(number))])
    except IndexError:
        print("The index error exist!")
    except FileNotFoundError:
        print("The specified file doesn't exist!")
    except PermissionError:
        print("You don't have permission to read from the file!")
    for el in formed_list:
        if (el.__eq__(formed_list[-1])):
            x = (el.index("\t"))
            str_out += el[x:]
        else:
            x = (el.index("\t"))
            y = (el.index("\n"))
            str_out = el[x:y]
    return str_out
