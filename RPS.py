


# To defeat all four opponents, your program may need
# to have multiple strategies
# that change depending on the plays of the opponent.


# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess

def beat(prev_play):
    return {"R": "P", "P": "S", "S": "R"}[prev_play]

def player(prev_play, opponent_history=[]):

    # player.pattern_tracker is a dictionary 
    # that tracks how often specific sequences of the opponent’s moves occur
    if not hasattr(player, 'pattern_tracker'):
        player.pattern_tracker = {}
        
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    pattern_tracker = player.pattern_tracker
    
    # n is the number of previous moves used for pattern matching
    # n = 4 is the best number of n but 5 is also good
    n = 4
    if len(opponent_history) > n:
        last_seq = "".join(opponent_history[-(n+1):])
        pattern_tracker[last_seq] = pattern_tracker.get(last_seq, 0) + 1

        potentials = [
            "".join([*opponent_history[-n:], v]) 
            for v in 'RPS'
        ]

        sub = {
            k: pattern_tracker[k]
            for k in potentials if k in pattern_tracker
        }

        pred = max(sub, key=sub.get)[-1:] if sub else 'P'
    else:
        pred = 'P'

    return beat(pred)


# Search best number of n  
def make_player(n):
    def player(prev_play, opponent_history=[]):
        if not hasattr(player, 'pattern_tracker'):
            player.pattern_tracker = {}
        if not prev_play:
            prev_play = 'R'
        opponent_history.append(prev_play)
        pt = player.pattern_tracker
        if len(opponent_history) > n:
            last_seq = ''.join(opponent_history[-(n+1):])
            pt[last_seq] = pt.get(last_seq, 0) + 1
            potentials = [''.join(opponent_history[-n:] + [v]) for v in 'RPS']
            sub = {k: pt[k] for k in potentials if k in pt}
            pred = max(sub, key=sub.get)[-1] if sub else 'P'
        else:
            pred = 'P'
        return beat(pred)
    return player