import os
import art
import random
def blackjack():
    os.system('cls')
    def reset():
        ch3 = input("\nRestart(r) or Exit(e) : ").lower()
        if ch3 == 'e':
            print("\n You Exited From The Game. Bye.👋\n")
            exit()
        else:
            os.system('cls')
            blackjack()

    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []

    # Draw 2 card for user
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
    user_score=sum(user_cards)

    print(f"\nThe cards in user's hand: {user_cards}      Score: {user_score}")

    # Draw 1 card for computer
    comp_cards.append(random.choice(cards))
    comp_score=sum(comp_cards)
    print(f"\nThe card in Computer's hand is: {comp_cards}      Score: {comp_score}")

    if 11 in user_cards:
        user_score=0
    if 11 in comp_cards:
        comp_score=0
    if user_score==0:
        print("\nYou Won!🎉 You have Blackjack.")
        reset()
    elif comp_score==0:
        print("\nYou Lost!💀 Computer has Blackjack")
        reset()
    elif user_score>21:
        print("\nYou Lost!💀 The Score is Exceeded.")
        reset()
    elif comp_score>21:
        print("\nYou Won!🎉 The Computer's Score is Exceeded.")
        reset()
    play=True
    while play:
        ch1 = input("\nDo you want to draw card(draw) or pass (pass) or exit (exit) : ").lower()
        if ch1 == "draw":
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)
            print(f"\nThe cards in user's hand: {user_cards}      Score: {user_score}")
            print(f"\nThe card in Computer's hand is: {comp_cards}      Score: {comp_score}")
            if 11 in user_cards:
                print("\nYou Won!🎉 You have Blackjack.")
                reset()
            elif user_score>21:
                print("\nYou Lost!💀 Score is exceeded.")
                reset()
        elif ch1=="pass":
            print(f"\nThe cards in user's hand: {user_cards}      Score: {user_score}")

            comp_cards.append(random.choice(cards))
            comp_score = sum(comp_cards)
            print(f"\nThe card in Computer's hand is: {comp_cards}      Score: {comp_score}")
            if 11 in comp_cards:
                print("\nYou Lost!💀 Computer has Blackjack.")
                reset()
            elif comp_score>21:
                print("\nYou Won!🎉 Computer's score is exceeded.")
                reset()
        else:
            if user_score==comp_score:
                print("\nIts Draw!🥳")
            elif user_score>comp_score:
                print("\nYou Won!🎉")
            elif comp_score>user_score:
                print("\nYou Lost!💀")
            reset()

ch=input("\nDo you Want to play the game ?(y/n): ").lower()
if ch=="y":
    blackjack()
else:
    exit(0)