#!/usr/bin/env python3


import random


moves = ["Rock", "Paper", "Scissors"]


class Player:
    def __init__(self):
        self.score = 0
    
    def move(self):
        return "Rock"

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "You"
    
    def move(self):
        choice = 0
        fails = 0
        while choice == 0:
            if fails == 0:
                move_choice = str(input("\nWhat will you throw: Rock, Paper, or Scissors? "))
            else:
                move_choice = str(input("\nTry again: Rock, Paper, or Scissors? "))
            if move_choice[0].upper() == "R":
                choice = "Rock"
            elif move_choice[0].upper() == "P":
                choice = "Paper"
            elif move_choice[0].upper() == "S":
                choice = "Scissors"
            else:
                if fails <= 2:
                    fails += 1
                    print(f"\n'Flag on the play! The referee rules that '{move_choice}' isn't a tournament-legal throw!'")
                else:
                    choice = random.choice(moves)
                    print(f"\n'The referee rules that the garbage you're throwing most closely resembles {choice}!'")
        return choice


class RockPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Dwayne Johnson"


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Henry Zebrowski"

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "John Kem Poe"


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "RoShamBot 3000"


def beats(one, two):
    return ((one == "Rock" and two == "Scissors") or
            (one == "Scissors" and two == "Paper") or
            (one == "Paper" and two == "Rock"))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print(f"That's a point for {self.p1.name}!")
        elif beats(move2, move1):
            self.p2.score += 1
            print(f"That's a point for {self.p2.name}!")
        else:
            print("It's a draw!""\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        round = 0
        print("\nGame start!")
        while self.p1.score <= 1 and self.p2.score <= 1:
            round += 1
            print(f"\nRound {round}:")
            self.play_round()
        if self.p1.score == 2:
            print(f"\n{self.p1.name} win! Congratulations!")
        else:
            print(f"\n{self.p2.name} wins! Better luck next time!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
