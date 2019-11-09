def steps(number, cnt=0):
    """Gets and prints the spreadsheet's header columns

    Args:
        file_loc (str): The file location of the spreadsheet
        print_cols (bool): A flag used to print the columns to the console
            (default is False)

    Returns:
        list: a list of strings representing the header columns
    """
    if number < 1:
        raise ValueError("invalid")
    elif number == 1:
        return cnt
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return steps(number, cnt + 1)
