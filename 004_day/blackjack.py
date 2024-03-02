import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

dealer_cards = []
player_cards = []


def generate_card():
    return random.choice(cards)

def card_sum(cards):
    _sum = 0
    for card in cards:
        _sum += card
    for card in cards:
        if _sum > 21 and 11 in cards:
            _sum -= 10
    return _sum


print("Welcome to the blackjack game")
while True:
    dealer_cards = [generate_card(), generate_card()]
    player_cards = [generate_card(), generate_card()]
    print(f"Dealer's first card: {dealer_cards[0]} --- sum: {dealer_cards[0]}")
    print(f"Your cards: {player_cards} --- sum: {card_sum(player_cards)}")
    while card_sum(player_cards) < 21:
        print("Do you want to draw another card? (y/n)")
        cont = input()
        if cont == "y":
            player_cards.append(generate_card())
            print(f"Your cards: {player_cards} --- sum: {card_sum(player_cards)}")
        elif cont == "n":
            break
        else:
            print("Invalid input")
    while card_sum(dealer_cards) < 17:
        dealer_cards.append(generate_card())
    print(f"Dealer's cards: {dealer_cards} --- sum: {card_sum(dealer_cards)}")
    if card_sum(player_cards) > 21:
        print("You lost")
    elif card_sum(dealer_cards) > 21:
        print("You won")
    elif card_sum(player_cards) > card_sum(dealer_cards):
        print("You won")
    elif card_sum(player_cards) == card_sum(dealer_cards):
        print("It's a draw")
    else:
        print("You lost")
    print("Do you want to play again? (y/n)")
    cont = input()
    if cont == "n":
        break
    elif cont == "y":
        continue
    else:
        print("Invalid input")
        break
print("Goodbye")
    
    