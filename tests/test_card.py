import unittest2
import card
import set


class TestCardMethods(unittest2.TestCase):
    def test_create_card(self):
        test_card = card.Card(0, 1, 2, 2)
        expected_result = 'blue $$$'
        self.assertEqual(str(test_card), expected_result)

    def test_card_equal(self):
        card_string = 'blue $$$'
        test_card_1 = set.create_cards(card_string)
        test_card_2 = set.create_cards(card_string)
        self.assertTrue(test_card_1 == test_card_2)

    def test_card_equal_fail(self):
        card_string_1 = 'blue $$$'
        test_card_1 = set.create_cards(card_string_1)
        card_string_2 = 'green #'
        test_card_2 = set.create_cards(card_string_2)
        self.assertNotEqual(str(test_card_1), str(test_card_2))

    def test_card_string(self):
        card_string = 'blue $$$'
        test_card = set.create_cards(card_string)
        self.assertEqual(str(test_card), card_string)


if __name__ == '__main__':
    unittest2.main()
