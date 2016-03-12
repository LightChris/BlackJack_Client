import random


class Card(object):
    """ Карты """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """ Возращает количество очков которое дает карта """
        if self.rank in "tjqk":
            # По 10 за десятку, валета, даму и короля
            return 10
        else:
            # Возвращает нужное число очков за любую другую карту
            # Туз изначально дает одно очко.
            return " a23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    """ Колода """

    def __init__(self):
        # ранги
        ranks = "23456789tjqka"
        # масти
        suits = "dchs"
        # генератор списков создающий колоду из 52 карт
        self.cards = [(s, r) for r in ranks for s in suits]
        # перетасовываем колоду. Не забудьте импортировать функцию shuffle из модуля random
        random.shuffle(self.cards)
        self.card_name = str(self.cards[-1][0] + self.cards[-1][1] + ".png")
        print(self.card_name)

    # def deal_card(self):
    #     """ Функция сдачи карты """
    #     return self.cards.pop()
