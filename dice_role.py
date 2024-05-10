import random


def roll():
    return random.randint(1, 6)


while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players should be more than 1 and less than 5, Try again !!!")
    else:
        print("Invalid input try again !!!")

players_score = [0 for _ in range(players)]
max_score = 50

while max(players_score) < max_score:
    for player_idx in range(players):
        score = 0
        while True:
            print("Player number", player_idx + 1, "turn")
            need_roll = input("Do you need to roll the dice (y/n): ").lower()
            if need_roll != "y":
                break
            value = roll()
            if value == 1:
                print("Your got 1 your turn is done!!!")
                break
            else:
                print("You have got ", value, "in the dice")
                score += value
                print("You current score is", score)
        players_score[player_idx] += score
        print("You total score is", players_score[player_idx])

win_score = max(players_score)
win_idx = players_score.index(win_score)
print("Player number", win_idx + 1, "with a score of", win_score)
