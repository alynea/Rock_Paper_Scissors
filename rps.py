"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = None
        self.their_move = None
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def increment_score(self):
        self.score += 1


""" Random player picks random moves in random"""


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))


"""Human Player recieves user input"""


class HumanPlayer(Player):
    def move(self):
        while True:
            userResponse = input("Pick Rock, Paper or Scissors\n").lower()
            if userResponse not in moves:
                print("Invalid Response. Select Rock, Paper or Response\n")
            else:
                break
        return userResponse


"""Cycle Player cycles through the moves list"""


class CyclePlayer(Player):
    cyclePlayer_move = ""

    def learn(self, my_move, their_move):
        self.cyclePlayer_move = my_move

    def move(self):
        if self.cyclePlayer_move == "scissors":
            self.cyclePlayer_move = "rock"
            return "rock"
        elif self.cyclePlayer_move == "rock":
            self.cyclePlayer_move = "paper"
            return "paper"
        elif self.cyclePlayer_move == "paper":
            self.cyclePlayer_move = "scissors"
            return "scissors"
        else:
            return "rock"


"""Reflect Player reflects the move of the other player"""


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move

    def move(self):
        if self.their_move is None:
            self.my_move = (random.choice(moves))
            return self.my_move
        else:
            return self.their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        isPlayerOneWin = beats(move1, move2)
        if isPlayerOneWin is True:
            print(f"Player 1 won!")
            self.p1.increment_score()
        elif move1 == move2:
            print(f"No winner in this round!")
        else:
            print(f"Player 2 won!")
            self.p2.increment_score()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        i = 0
        while True:
            newRound = input("Would you like to play? Y/N\n").upper()
            if newRound == "Y":
                i += 1
                print(f"Round {i}:")
                self.play_round()
            elif newRound == "N":
                print("Game over!")
                break
            else:
                print("Invalid input. Enter Y/N\n")


if __name__ == '__main__':
    player1 = RandomPlayer()
    player2 = HumanPlayer()
    game = Game(player1, player2)
    game.play_game()
    print(f"Player 1 score:{player1.score} and Player 2 score:{player2.score}")
