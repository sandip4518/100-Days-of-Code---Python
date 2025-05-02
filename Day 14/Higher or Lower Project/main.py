import art
import game_data
import random
print(art.logo)
play=True
ran_choice1 = random.choice(game_data.data)
score=0
while play:
    print(f"A: {ran_choice1['name']}, A {ran_choice1['description']} from {ran_choice1['country']}.")
    print(art.vs)
    ran_choice2 = random.choice(game_data.data)
    print(f"B: {ran_choice2['name']}, A {ran_choice2['description']} from {ran_choice2['country']}.")

    ch = input("\nWho has most followers 'A' or 'B' : ").upper()

    if ch == 'A':
        if ran_choice1['follower_count'] > ran_choice2['follower_count']:
            print("Yes right")
            ran_choice1=ran_choice2
            score+=1
            print(f"Your Score: {score}")
        else:
            print("\nWrong Answer")
            play=False
            print(f"Your final score: {score}")
    else:
        if ran_choice1['follower_count'] < ran_choice2['follower_count']:
            print("Yes right")
            ran_choice1=ran_choice2
            score+=1
            print(f"Your Score: {score}")
        else:
            print("\nWrong Answer")
            play=False
            print(f"Your final score: {score}")
