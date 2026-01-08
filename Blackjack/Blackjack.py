import random
from ascii_art import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_check(hand): # To check and adjust the value of ACE in Deck
    score = sum(hand)
    index = 0
    for i in hand:
        if score > 21:
            if i == 11:
                hand[index] = 1
                index += 1
                score = sum(hand)
        
def score_check(player_hand, computer_hand, player_score, computer_score):  # To check Who is the winner
    print(f"Your final Hand: {player_hand}, Final Score: {player_score}")
    print(f"Computer's final Hand: {computer_hand}, Final Score: {computer_score}\n")
    if player_score > 21:
        print("You went Over")
        print("You Lose")
    elif player_score == computer_score:
        print("It's a DRAWWWWW!!")
    elif computer_score == 21:
        print("COMPUTER's BLACKJACK")
        print("You Lose!")
    elif player_score == 21:
        print("BLACKJACK !!!")
        print("You won!!!")
    elif player_score > computer_score:
        print("You got a upper Hand!!")
        print("You won")
    else:
        print("Computer Won!")
        print("Better luck next time!")
        
def game_mechanics():   # Main Game Mechanics
    p_hand = [random.choice(cards), random.choice(cards)]
    c_hand = [random.choice(cards), random.choice(cards)]
    ace_check(p_hand)
    ace_check(c_hand)
    p_score = sum(p_hand)
    c_score = sum(c_hand)
    print(f"Your Hand: {p_hand}, Your Total Score: {p_score}\nComputer's First card: {c_hand[0]}\n")
    deal = True
    while deal:
        want_card = input("Do you want to deal a card?('y' for yes and 'n' to pass): ").lower()
        if want_card == "y":
            new_card = random.choice(cards)
            p_hand.append(new_card)
            ace_check(p_hand)
            p_score = sum(p_hand)
            print(f"Your Hand: {p_hand}, Your Total Score: {p_score}\nComputer's First card: {c_hand[0]}\n")
            if p_score > 21:
                score_check(player_hand = p_hand, computer_hand = c_hand, player_score = p_score, computer_score = c_score)
                deal = False
        else:
            deal = False
            score_check(player_hand = p_hand, computer_hand = c_hand, player_score = p_score, computer_score = c_score)
    
playing = True

while playing:

    play = input("\nDO you want to play BlackJack?: ('y' for YES and 'n' for NO): ").lower()
    if play == "y":
        print(art)
        game_mechanics()
    else:
        playing = False
        print("Thanks for Coming!")