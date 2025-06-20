# To defeat all four opponents, your program may need
# to have multiple strategies
# that change depending on the plays of the opponent.

## Randomly


def random_strat():
    return random.choice(["R", "P", "S"])


## Anti-repetition - Quincy


def anti_repetition_strat(opponent_history):
    pass


## frequency Analysis - Mrugesh


def frequency_strat(opponent_history):
    pass


## Markov chain Models - Abbey


def markov_chain_strat(opponent_history):
    pass


## pattern - Kris
def pattern_strat(opponent_history):
    pass


# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
