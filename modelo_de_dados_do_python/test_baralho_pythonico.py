import unittest
from baralho_pythonico import Card, FrenchDeck

class TestDeck(unittest.TestCase):
    def test_create_card(self):
        card = Card('7', 'diamonds')
        self.assertEqual(card.rank, '7')
        self.assertEqual(card.suit, 'diamonds')

    def test_len(self):
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)

    def test_getitem(self):
        deck = FrenchDeck()
        self.assertEqual(deck[0], Card('2', 'spades'))
        self.assertEqual(deck[-1], Card('A', 'hearts'))

    def test_contains(self):
        deck = FrenchDeck()
        self.assertIn(Card('A', 'hearts'), deck)

if __name__ == '__main__':
    unittest.main()