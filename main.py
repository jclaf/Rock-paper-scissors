# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player, make_player
from unittest import main

play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)

# for n in range(2, 9):
#   player = make_player(n)
#   win_rates = []
#   for bot in [quincy, abbey, kris, mrugesh]:
#       win_rates.append(play(player, bot, 1000))
#   print(f"n={n}: Quincy={win_rates[0]:.1f}%, Abbey={win_rates[1]:.1f}%, Kris={win_rates[2]:.1f}%, Mrugesh={win_rates[3]:.1f}%")

# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)