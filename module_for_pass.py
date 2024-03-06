from random import randint


def random_number_list() -> list:
    """
    Function builds list of 5-digit numbers
    :return: list with length of 6 (6 number in list)
    """
    rnd_list = []
    for _ in range(6):
        rnd_num = 0
        for i in range(0, 5):
            rnd = randint(1, 6)
            rnd_num += rnd * (10 ** i)

        rnd_list.append(rnd_num)
    return rnd_list


def user_num_in_out_txt(list_of_nums) -> str:
    """
    Function gets list of number with length 6
    :list_of_nums: a 3-number list
    :return: string of three words without spaces
    """
    out_str = ""
    number_digits = len(list_of_nums)
    if (number_digits != 6):
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
