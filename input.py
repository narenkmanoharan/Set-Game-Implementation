import set
import sys


def input_filename():
    """
    Function to input the filename from the handle the input from the user
    """
    while True:
        input_val = input("Please enter option: ")
        if input_val == "1":
            filename = input("\nPlease enter the filename: ")
            if not filename.endswith(".txt"):
                print("\nPlease check the filename given. It needs to be a txt file.")
            return filename
        elif input_val == "2":
            sys.exit()
        else:
            print("\nPlease enter valid option!\n")


def read_from_file(filename):

    """
    Function to read the lines from the input file and create new Card object for each line read
    :rtype: List of Card objects
    """
    card_list = []
    try:
        file = open(filename, "r")
    except:
        print("\nPlease check if the file inside the code folder\n")
        input_filename()
    else:
        for card_string in file:
            cards = set.create_cards(card_string)
            if cards is not None:
                card_list.append(cards)
        return card_list

