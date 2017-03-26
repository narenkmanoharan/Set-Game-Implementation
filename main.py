import input
import os
import set


def main():
    print("Welcome to the set game!\n\nPlease don't forget to move the input file into the 'code' folder!\n\nEnter 1 to Enter the filename (Eg: input1.txt) \nEnter 2 to Exit\n")
    filename = input.input_filename()
    filepath = os.path.dirname(__file__) + "/" + filename
    card_list = input.read_from_file(filepath)
    set_cards = set.check_combination(card_list)
    print()
    print(len(set_cards))
    largest_disjoint_set = set.find_largest_disjoint_set(set_cards)
    print(len(largest_disjoint_set))
    print()
    for each_set in largest_disjoint_set:
        print(each_set[0])
        print(each_set[1])
        print(each_set[2])
        print()


if __name__ == '__main__':
    main()
