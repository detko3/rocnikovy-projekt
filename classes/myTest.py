from .card import Card
from classes.player import print_cards

allSets = []

def createCustom(cards):
    jokers = []
    heart = []
    spade = []
    diamond = []
    club = []
    for card in cards:
        if card.value == 0:
            jokers.append(card)
        elif card.symbol == "♥":
            heart.append(card)
        elif card.symbol == "♠":
            spade.append(card)
        elif card.symbol == "♦":
            diamond.append(card)
        elif card.symbol == "♣":
            club.append(card)

    hand = [jokers, heart, spade, diamond, club]
    for h in hand:
        if len(h):
            h.sort(key=lambda item: item.value)

    allCards = []
    # print_cards(heart)
    # TODO prvy krat iba pre zolika
    if len(jokers) > 0 and heart[0].value != 1:
        allCards += create_forward([Card(0, "")], heart, len(jokers) - 1, 1)
    for i in range(0, len(heart)):
        allCards = allCards + create_forward([heart[i]], heart[i + 1: len(heart)], len(jokers), 0)
        if i < len(heart) - 1:
            if len(jokers) > 0 and heart[i + 1].value != 1:
                allCards = allCards + create_forward([Card(0, "")], heart[i + 1: len(heart)], len(jokers) - 1, 1)
    # print(allCards)
    return allCards

def create_forward(usedCards, cards, jokers, usedJokers):
    #TODO usecase Acko moze ist na koniec
    newSets = []
    usedJokersOnEnd = 0
    lastNonJokerVal = -1
    for card in reversed(usedCards):
        if card.value != 0:
            lastNonJokerVal = card.value
            break
        else:
            usedJokersOnEnd += 1

    if usedJokersOnEnd == 1 and len(usedCards) == 3 and usedJokers == 1:
        newSets.append(usedCards.copy())

    if len(usedCards) > 3 and usedCards[0].value == 0:
        return []

    for i in range(0, len(cards)):
        if lastNonJokerVal == -1:
            usedCards.append(cards[i])
            lastNonJokerVal = cards[i].value
            usedJokersOnEnd = 0
        elif cards[i].value == lastNonJokerVal + 1 + usedJokersOnEnd:
            if jokers > 0:
                cp = usedCards.copy()
                cp.append(Card(0, ""))
                newSets += create_forward(cp, cards[i + 1: len(cards)], jokers - 1, usedJokers + 1)
            usedCards.append(cards[i])
            lastNonJokerVal = cards[i].value
            usedJokersOnEnd = 0
            if len(usedCards) > 3 and usedCards[0].value == 0:
                return newSets
            elif len(usedCards) > 2:
                newSets.append(usedCards.copy())
        elif cards[i].value <= lastNonJokerVal + 1 + usedJokersOnEnd + jokers and cards[i]. value > lastNonJokerVal + 1 + usedJokersOnEnd:
            num = 0
            while cards[i].value != lastNonJokerVal + 1 + usedJokersOnEnd + num:
                usedCards.append(Card(0, ""))
                num += 1
                jokers -= 1
            if jokers > 0:
                cp2 = usedCards.copy()
                cp2.append(Card(0, ""))
                newSets += create_forward(cp2, cards[i + 1: len(cards)], jokers - 1, usedJokers + 1 + num)
            usedCards.append(cards[i])
            lastNonJokerVal = cards[i].value
            usedJokersOnEnd = 0
            newSets.append(usedCards.copy())

    return newSets
