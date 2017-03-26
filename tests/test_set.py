import unittest
import set


class TestSETMethods(unittest.TestCase):
    def test_create_cards_1(self):
        card_string = 'blue #'
        card_obj = set.create_cards(card_string)
        self.assertEqual(card_obj.color, 0)
        self.assertEqual(card_obj.symbol, 2)
        self.assertEqual(card_obj.shading, 2)
        self.assertEqual(card_obj.number, 0)

    def test_create_cards_2(self):
        card_string = 'green @@@'
        card_obj = set.create_cards(card_string)
        self.assertEqual(card_obj.color, 1)
        self.assertEqual(card_obj.symbol, 0)
        self.assertEqual(card_obj.shading, 2)
        self.assertEqual(card_obj.number, 2)

    def test_create_third_card_1(self):
        card_string = ['blue #', 'green @@@']
        first_card = set.create_cards(card_string[0])
        second_card = set.create_cards(card_string[1])
        expected_card = 'yellow $$'
        third_card = set.create_third_card(first_card, second_card)
        self.assertEqual(str(third_card), expected_card)

    def test_create_third_card_2(self):
        card_string = ['yellow #', 'blue $']
        first_card = set.create_cards(card_string[0])
        second_card = set.create_cards(card_string[1])
        expected_card = 'green @'
        third_card = set.create_third_card(first_card, second_card)
        self.assertEqual(str(third_card), expected_card)


if __name__ == '__main__':
    unittest.main()
