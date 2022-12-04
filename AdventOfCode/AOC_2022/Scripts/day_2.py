import os
import sys
from enum import Enum
with open(os.path.join(sys.path[0], "../Inputs/input_day_2.txt"), "r") as my_input:
    _INPUT = my_input.read()
    _INPUT = _INPUT.split("\n")
    # print(_INPUT)


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RoundValue(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


ChoiceDict = {
    'A': Choice.ROCK,
    'B': Choice.PAPER,
    'C': Choice.SCISSORS,
    'X': Choice.ROCK,
    'Y': Choice.PAPER,
    'Z': Choice.SCISSORS
}


class Scoreboard():

    def __init__(self):
        self._player_score = 0

    @ property
    def PLAYER_SCORE(self):
        return self._player_score

    @ PLAYER_SCORE.setter
    def PLAYER_SCORE(self, value):
        self._player_score = value

    def _shuffle_choice(self, opp_choice, game_condition):
        # X needs to lose
        if game_condition == Choice.ROCK:
            if opp_choice == Choice.ROCK:
                return Choice.SCISSORS
            elif opp_choice == Choice.PAPER:
                return Choice.ROCK
            elif opp_choice == Choice.SCISSORS:
                return Choice.PAPER

        # Y needs to draw
        if game_condition == Choice.PAPER:
            return opp_choice

        # Z needs to Win
        if game_condition == Choice.SCISSORS:
            if opp_choice == Choice.ROCK:
                return Choice.PAPER
            elif opp_choice == Choice.PAPER:
                return Choice.SCISSORS
            elif opp_choice == Choice.SCISSORS:
                return Choice.ROCK

    def playGame(self, opponent_choice, player_choice, part_two=True):

        if part_two:
            new_choice = self._shuffle_choice(opponent_choice, player_choice)
            player = new_choice.value
        else:
            player = player_choice.value

        opponent = opponent_choice.value
        self.PLAYER_SCORE += player

        if opponent == player:
            self.PLAYER_SCORE += RoundValue.DRAW.value
        elif opponent == Choice.ROCK.value:
            if player == Choice.PAPER.value:
                self.PLAYER_SCORE += RoundValue.WIN.value
            elif player == Choice.SCISSORS.value:
                self.PLAYER_SCORE += RoundValue.LOSE.value
        elif opponent == Choice.PAPER.value:
            if player == Choice.ROCK.value:
                self.PLAYER_SCORE += RoundValue.LOSE.value
            elif player == Choice.SCISSORS.value:
                self.PLAYER_SCORE += RoundValue.WIN.value
        elif opponent == Choice.SCISSORS.value:
            if player == Choice.ROCK.value:
                self.PLAYER_SCORE += RoundValue.WIN.value
            elif player == Choice.PAPER.value:
                self.PLAYER_SCORE += RoundValue.LOSE.value


# ------------ Part 1 --------------- #
SCORE1 = Scoreboard()
for i in _INPUT:
    value_pair = i.split(" ")
    SCORE1.playGame(ChoiceDict[value_pair[0]],
                    ChoiceDict[value_pair[1]], False)
print("Part 1 Answer: {}".format(SCORE1.PLAYER_SCORE))
# Should output 14163

# ------------ Part 2 --------------- #

SCORE2 = Scoreboard()
for i in _INPUT:
    value_pair = i.split(" ")
    SCORE2.playGame(ChoiceDict[value_pair[0]],
                    ChoiceDict[value_pair[1]], True)
print("Part 2 Answer: {}".format(SCORE2.PLAYER_SCORE))
# Should output 12091
