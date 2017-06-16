from copy import copy, deepcopy
from random import shuffle, choice

from sushigo.cards import Card, MakiCard, SashimiCard, WasabiCard, DumplingCard, PuddingCard, NigiriCard, TempuraCard


class Deck:

    def __init__(self, *cards):
        for card in cards:
            if not isinstance(card, Card):
                raise TypeError('Deck only accepts objects of type Card.')
        self.cards = None
        self.initial_cards = cards
        self.reset()

    @classmethod
    def create(cls, card_types, card_counts):
        if len(card_types) != len(card_counts):
            raise ValueError('card_counts must have the same length as card_types')
        return cls(*cls.create_card_list(card_types, card_counts))

    @staticmethod
    def create_card_list(card_types, card_counts):
        return [copy(card_type) for card_type, count in zip(card_types, card_counts) for _ in range(count)]

    def reset(self):
        self.cards = deepcopy(self.initial_cards)
        shuffle(self.cards)

    def __next__(self):
        if len(self.cards) == 0:
            raise StopIteration
        return self.cards.pop()


class InfiniDeck(Deck):

    def reset(self):
        pass

    def __next__(self):
        return choice(self.initial_cards)


class StandardDeck(Deck):

    def __init__(self, n_decks=1):
        card_types = (MakiCard(1), MakiCard(2), MakiCard(3), PuddingCard(),
                      NigiriCard('egg'), NigiriCard('salmon'), NigiriCard('squid'),
                      TempuraCard(), SashimiCard(), DumplingCard(), WasabiCard())
        card_counts = [i*n_decks for i in (7, 7, 7, 8, 6, 6, 5, 10, 10, 15, 4)]
        super().__init__(*self.create_card_list(card_types, card_counts))
