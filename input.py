import set


def input_filename():
    """
    Function to input the filename from the handle the input from the user
    """
    filename = input("Please enter the filename (Eg: input1.txt): ")
    if not filename.endswith(".txt"):
        print("\nPlease check the filename given. It needs to be a txt file.")
    return filename


def read_from_file(filename):
    """
    Function to read the lines from the input file and create new Card object for each line read
    :rtype: List of Card objects
    """
    card_list = []
    try:
        file = open(filename, "r")
        for card_string in file:
            cards = set.create_cards(card_string)
            if cards is not None:
                card_list.append(cards)
        return card_list
    except:
        print("\nPlease check if the file inside the code folder\n")
        input_filename()        
