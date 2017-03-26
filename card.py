class Card:
    def __init__(self, color=None, symbol=None, shading=None, number=None):
        """
        Initializing the Card with the given values
        """
        self.color = color
        self.symbol = symbol
        self.shading = shading
        self.number = number

    def __eq__(self, other):
        """
        Function to check the equality of two cards
        :rtype: Boolean
        """
        if self.number == other.number and self.symbol == other.symbol and \
                self.color == other.color and self.shading == other.shading:
            return True
        else:
            return False

    def __str__(self):
        """
        Function to represent the given 'card' in a string representation
        :rtype: String
        """
        if self.color == 0:
            color = "blue"
        elif self.color == 1:
            color = "green"
        else:
            color = "yellow"
        if self.symbol == 0:
            symbol = 'A'
        elif self.symbol == 1:
            symbol = 'S'
        else:
            symbol = 'H'
        number = self.number + 1
        if self.shading == 0:
            attribute = (symbol * number).lower()
        elif self.shading == 1:
            attribute = (symbol * number).upper()
        else:
            if symbol == 'A':
                attribute = '@' * number
            elif symbol == 'S':
                attribute = '$' * number
            else:
                attribute = '#' * number
        card_string = color + " " + attribute
        return card_string
