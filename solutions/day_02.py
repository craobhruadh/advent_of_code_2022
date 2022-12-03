from enum import Enum

# There is probably a way to encode this data better
# Coding up data structures as AoC problems are revealed is clunky


class Move(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class TheirMove(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class Scores(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSS = 0
    DRAW = 3
    WIN = 6


class Outcome(Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    output = []
    for line in lines:
        tokens = line.split()
        output.append((tokens[0], tokens[1]))
    return output


def evaluate_move_one(move):
    score = 0
    # There is definitely a better way to encode this - a matrix?
    if move[1] == Move.ROCK.value:
        score += Scores.ROCK.value
    elif move[1] == Move.PAPER.value:
        score += Scores.PAPER.value
    elif move[1] == Move.SCISSORS.value:
        score += Scores.SCISSORS.value
    if move[0] == TheirMove.ROCK.value:
        if move[1] == Move.ROCK.value:
            score += Scores.DRAW.value
        elif move[1] == Move.PAPER.value:
            score += Scores.WIN.value
        elif move[1] == Move.SCISSORS.value:
            score += Scores.LOSS.value
    elif move[0] == TheirMove.PAPER.value:
        if move[1] == Move.ROCK.value:
            score += Scores.LOSS.value
        elif move[1] == Move.PAPER.value:
            score += Scores.DRAW.value
        elif move[1] == Move.SCISSORS.value:
            score += Scores.WIN.value
    elif move[0] == TheirMove.SCISSORS.value:
        if move[1] == Move.ROCK.value:
            score += Scores.WIN.value
        elif move[1] == Move.PAPER.value:
            score += Scores.LOSS.value
        elif move[1] == Move.SCISSORS.value:
            score += Scores.DRAW.value
    return score


def evaluate_move_two(move):
    score = 0
    their_move, needed_outcome = TheirMove(move[0]), Outcome(move[1])

    if needed_outcome.name == Outcome.WIN.name:
        score += Scores.WIN.value
        if their_move.name == 'ROCK':
            score += Scores.PAPER.value
        elif their_move.name == 'PAPER':
            score += Scores.SCISSORS.value
        elif their_move.name == 'SCISSORS':
            score += Scores.ROCK.value
    elif needed_outcome.name == Outcome.LOSE.name:
        score += Scores.LOSS.value
        if their_move.name == 'ROCK':
            score += Scores.SCISSORS.value
        elif their_move.name == 'PAPER':
            score += Scores.ROCK.value
        elif their_move.name == 'SCISSORS':
            score += Scores.PAPER.value
    elif needed_outcome.name == Outcome.DRAW.name:
        score += Scores.DRAW.value
        if their_move.name == 'ROCK':
            score += Scores.ROCK.value
        elif their_move.name == 'PAPER':
            score += Scores.PAPER.value
        elif their_move.name == 'SCISSORS':
            score += Scores.SCISSORS.value

    return score


def problem_one(data):
    total = 0
    for d in data:
        total += evaluate_move_one(d)
    return total


def problem_two(data):
    total = 0
    for d in data:
        total += evaluate_move_two(d)
    return total


if __name__ == "__main__":
    data = read_file('./data/day_two.txt')
    print(problem_one(data))
    print(problem_two(data))
