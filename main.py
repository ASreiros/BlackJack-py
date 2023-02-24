import copy
import random

import logo
import  carddeck
from copy import deepcopy

my_deck = []


def deal_card():
    card = random.choice(my_deck)
    my_deck.remove(card)
    return card

def blackjack():
    print(logo.logo)
    print("     Welcome to BLACKJACK        ")
    player_card_names = []
    player_card_values = []
    dealer_card_names = []
    dealer_card_values = []
    for n in range(2):
        player_card = deal_card()
        dealer_card = deal_card()
        player_card_names.append(player_card['name'])
        player_card_values.append(player_card['value'])
        dealer_card_names.append(dealer_card['name'])
        dealer_card_values.append(dealer_card['value'])
        dealer_card_names_hidden = copy.deepcopy(dealer_card_names)
        dealer_card_values_hidden = copy.deepcopy(dealer_card_values)
        dealer_card_names_hidden[0] = "*"
        dealer_card_values_hidden[0] = "*"

    player_stop = False
    dealer_stop = False
    blackjack_clause = False

    while player_stop is False:
        if sum(player_card_values) == 21 and len(player_card_values) == 2:
            blackjack_clause = True
            player_stop = True
        aces = True
        while sum(player_card_values) > 21 and aces is True:
            if 11 in player_card_values:
                player_card_values[player_card_values.index(11)] = 1
            else:
                aces = False
                player_stop = True

        print(f"Your cards:        {player_card_names}")
        print(f"Your cards values: {player_card_values}, your total :{sum(player_card_values)}")
        print("         ")
        print(f"Dealer cards:        {dealer_card_names_hidden}")
        print(f"Dealer cards values: {dealer_card_values_hidden}, dealer total :{dealer_card_values_hidden[1]}")

        if sum(player_card_values) <= 21 and blackjack_clause is False:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                player_card = deal_card()
                player_card_names.append(player_card['name'])
                player_card_values.append(player_card['value'])
                print("-------------------------------------")
            else:
                player_stop = True
        elif blackjack_clause == True:
            print("You have blackjack!!! Congratulations!!!")
        else:
            print("You went over the top")

    while dealer_stop is False and not blackjack_clause:
        aces = True
        while sum(dealer_card_values) > 21 and aces is True:
            if 11 in dealer_card_values:
                dealer_card_values[dealer_card_values.index(11)] = 1
            else:
                aces = False
                dealer_stop = True

        print(f"Your cards:        {player_card_names}")
        print(f"Your cards values: {player_card_values}, your total :{sum(player_card_values)}")
        print("         ")
        print(f"Dealer cards:        {dealer_card_names}")
        print(f"Dealer cards values: {dealer_card_values}, dealer total :{sum(dealer_card_values)}")

        if sum(player_card_values) > 21:
            dealer_stop = True
        elif sum(dealer_card_values) <= 21:
            if sum(dealer_card_values) < 17:
                dealer_card = deal_card()
                dealer_card_names.append(dealer_card['name'])
                dealer_card_values.append(dealer_card['value'])
                print("-------------------------------------")
            else:
                dealer_stop = True
        else:
            print("Dealer went over the top")

    result_text = ""
    if blackjack_clause:
        if dealer_card_values == 21 and len(dealer_card_values) == 2:
            result_text = "It is a DRAW. You have same both collected Blackjack."
        else:
            result_text = "You win. You have blackjack"
    elif sum(player_card_values) > 21:
        result_text = "You lose. You went over 21."
    elif sum(dealer_card_values) > 21:
        result_text = "You win. Dealer went over 21."
    elif sum(dealer_card_values) > sum(player_card_values):
        result_text = "You lost. Dealer has more points."
    elif sum(dealer_card_values) < sum(player_card_values):
        result_text = "You Win. You have more points."
    elif sum(dealer_card_values) == sum(player_card_values):
        result_text = "It is a DRAW. You have same amount of points."
    else:
        print("Something was not planned. Else clause")

    print(f"Your total score is {sum(player_card_values)}. Dealer total score is {sum(dealer_card_values)}. {result_text}")


play = True
while play:
    if input("Do you want to play the BLACKJACK game? Please type 'y' for yes or 'n' for no: ") == 'y':
        my_deck = copy.deepcopy(carddeck.deck)
        blackjack()
    else:
        print("Have a good day. Program will exit now")
        play = False
