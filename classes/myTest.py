import copy

from .card import Card
from classes.player import print_cards

allSets = []

def createCustom(cards):
    heart = []
    spade = []
    diamond = []
    club = []
    for card in cards:
        if card.symbol == "♥":
            heart.append(card)
        elif card.symbol == "♠":
            spade.append(card)
        elif card.symbol == "♦":
            diamond.append(card)
        elif card.symbol == "♣":
            club.append(card)

    hand = [heart, spade, diamond, club]
    for h in hand:
        if len(h):
            h.sort(key=lambda item: item.value)

    allCards = []
    # print_cards(heart)
    for h in hand:
        hasA = False
        if len(h) > 0:
            if h[0].value == 1:
                hasA = True
        for i in range(0, len(h)):
            allCards += create_forward(h[i], h[i + 1 : len(h)], hasA)
    allCards += createPairs(hand)

    return allCards


def create_forward(card, cards, hasA):
    if len(cards) < 2 and not hasA:
        return []

    usedCards = [card]
    result = []

    for tmpCard in cards:
        if card.value + 1 == tmpCard.value:
            usedCards.append(tmpCard)
            card = tmpCard
            if len(usedCards) >= 6:
                return result
            if len(usedCards) > 2:
                result.append(usedCards.copy())
        elif card.value + 1 < tmpCard.value:
            return result

    if card.value == 13 and hasA and usedCards[0].value != 1:
        usedCards.append(Card(1, card.symbol))
        if len(usedCards) > 2 and len(usedCards) < 6:
            result.append(usedCards.copy())

    return result

def createPairs(hand):
    result = []
    for i in range(1, 14):
        usedCards = []
        if containsValue(i, hand[0]):
            usedCards.append(Card(i, hand[0][0].symbol))
        if containsValue(i, hand[1]):
            usedCards.append(Card(i, hand[1][0].symbol))
        if len(usedCards) == 0:
            # print("END HERE")
            continue
            # return result

        if containsValue(i, hand[2]):
            usedCards.append(Card(i, hand[2][0].symbol))
        if containsValue(i, hand[3]):
            usedCards.append(Card(i, hand[3][0].symbol))

        if len(usedCards) == 4:
            result.append(usedCards.copy())
            for j in range(0, 4):
                cp = usedCards.copy()
                cp.pop(j)
                result.append(cp)
        if len(usedCards) == 3:
            result.append(usedCards.copy())

    return result


def containsValue(value, arr):
    for item in arr:
        if item.value == value:
            return True
        elif item.value > value and value != 1:
            return False
    return False


def containsValueAndSymbol(value, symbol, arr):
    for item in arr:
        if item.value == value and item.symbol == symbol:
            return True
        elif item.value > value and value != 1:
            return False
    return False

def startCombinigSets(allSets, hand):
    # pouzijem allSets[0] este pridat moznost ked nepouzijem allSets[0]
    result = []
    for i in range(0, len(allSets)):
        newSet = combineSets(allSets[i], allSets[i + 1: len(allSets)], hand)
        if isinstance(newSet[0], Card):
            # print("here")
            newSet = [[newSet]]
    # print(newSet)
        for first in newSet:
            # for it in first:
                # print_cards(it)
            sumOfSet = countCardSet(first)
            # print(sumOfSet)
            if sumOfSet >= 51:
                result.append(first)
            # print("/////////////////////////////////////")
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    return result

def combineSets(currSet, allSets, hand):
    # print("Combine set")
    # print_cards(currSet)
    result = []

    for card in currSet:
        num = 0
        for h in hand:
            if h.value == card.value and h.symbol == card.symbol:
                num += 1
        if num < 2:
            allSets = removeFromSet(card, allSets)

    hand = removeFromHand(currSet, hand)

    if len(allSets) == 0:
        return currSet

    for i in range(0, len(allSets)):
        res = combineSets(allSets[i], allSets[i + 1: len(allSets)], hand)
        if isinstance(res[0], Card):
            res1 = [currSet]
            res1.append(res)
            result.append(res1)
        else:
            for item in res:

                res1 = [currSet]
                res1 += item
                result.append(res1)

    return result

def removeFromSet(card, allSets):
    return [item for item in allSets if not containsValueAndSymbol(card.value, card.symbol, item)]

def removeFromHand(cards ,hand):
    return [card for card in hand if not containsValueAndSymbol(card.value, card.symbol, cards)]

def countCardSet(cardsSet):
    count = 0
    for cards in cardsSet:
        for i in range(0, len(cards)):
            if cards[i].value == 1:
                if i == 0 and cards[1].value == 2:
                    count = count + 1
                else:
                    count = count + 10
            elif cards[i].value > 9:
                count = count + 10
            else:
                count = count + cards[i].value
    return count

def cardsProbability(cardsSet, valueDict):
    probability = 1
    valueDictCopy = copy.deepcopy(valueDict)
    for cards in cardsSet:
        for card in cards:
            dictNum = -1
            if card.symbol == "♠":
                dictNum = 0
            elif card.symbol == "♣":
                dictNum = 1
            elif card.symbol == "♥":
                dictNum = 2
            elif card.symbol == "♦":
                dictNum = 3
            # print(dictNum)
            probability = probability * valueDictCopy[dictNum][card.value].pop()

    return probability

def fillDict(hand, values):
    dicts = []
    for i in range(0, 4):
        dicts.append({})
    for i in range(0, len(values)):
        if isinstance(hand[i], Card):
            dictNum = -1
            if hand[i].symbol == "♠":
                dictNum = 0
            elif hand[i].symbol == "♣":
                dictNum = 1
            elif hand[i].symbol == "♥":
                dictNum = 2
            elif hand[i].symbol == "♦":
                dictNum = 3
            if hand[i].value in dicts[dictNum]:
                if dicts[dictNum][hand[i].value][0] > values[i]:
                    dicts[dictNum][hand[i].value].insert(0, values[i])
                else:
                    dicts[dictNum][hand[i].value].append(values[i])
            else:
                dicts[dictNum][hand[i].value] = [values[i]]
    return dicts


def filterCards(custom, hand, prob):
    # print("----------------------------------")
    # for car in custom:
    #     print_cards(car)
    # # print(custom)
    # print("----------------------------------")

    filteredSets = startCombinigSets(custom, hand)
    dict = fillDict(hand, prob)
    highestIndex = -1
    highestNum = -1
    for i in range(0, len(filteredSets)):
        cardsProb = cardsProbability(filteredSets[i], dict)
        if cardsProb > highestNum:
            highestNum = cardsProb
            highestIndex = i

    if len(filteredSets):
        return filteredSets[highestIndex]
    return []


def filterCardsNotFirst(custom, hand, prob):
    # print("----------------------------------")
    # for car in custom:
    #     print_cards(car)
    # # print(custom)
    # print("----------------------------------")
    dict = fillDict(hand, prob)
    highestIndex = -1
    highestNum = -1

    for i in range(0, len(custom)):
        cardsProb = cardsProbability([custom[i]], dict)
        if cardsProb > highestNum:
            highestNum = cardsProb
            highestIndex = i

    if len(custom):
        return custom[highestIndex]
    else:
        return []


