# Rock Paper Scissors AI
Ce code implémente une intelligence artificielle jouant à pierre-papier-ciseaux, capable de battre plusieurs bots en adaptant sa stratégie grâce à une chaîne de Markov.

## Fonctionnalités principales
Analyse les séquences de coups de l’adversaire pour anticiper ses prochains choix.

Utilise une chaîne de Markov : les probabilités de transition entre séquences de coups sont exploitées pour prédire le prochain coup adverse.

S’adapte dynamiquement à différents styles de bots grâce à ce modèle probabiliste.

Permet de tester différentes profondeurs d’analyse (paramètre n) pour optimiser la prédiction.

Utilise une fonction beat() pour toujours choisir le coup gagnant face à la prédiction adverse.

## Algorithme utilisé
Chaîne de Markov : le programme enregistre les séquences récentes de coups de l’adversaire et compte leur fréquence, modélisant ainsi les transitions entre états (séquences de coups).

Prédiction : pour chaque tour, la prochaine action de l’adversaire est prédite à partir de la séquence la plus probable selon la chaîne de Markov construite à partir de l’historique.

Adaptation : la stratégie s’ajuste en temps réel selon l’historique observé.

### 1. Fonction principale : player
Cette fonction gère chaque coup joué par l’IA.

````python
def player(prev_play, opponent_history=[]):
    # ... (voir le code fourni)
````
Entrée : dernier coup de l’adversaire (prev_play), historique des coups.

Stockage : mémorise les séquences de coups dans un dictionnaire, modélisant les transitions de la chaîne de Markov.

Prédiction : anticipe le prochain coup de l’adversaire selon la séquence la plus probable.

Action : joue le coup qui bat la prédiction.

### 2. Fonction utilitaire : beat
Détermine le coup gagnant face à un coup donné.

````python
def beat(prev_play):
    return {"R": "P", "P": "S", "S": "R"}[prev_play]
````
### 3. Fonction avancée : make_player(n)
Permet de générer une IA avec une profondeur d’analyse personnalisée.

````python
def make_player(n):
    # ... (voir le code fourni)
````
Exemple d’utilisation

````python
from RPS import player, make_player

# Pour jouer un match de 1000 parties contre un bot "quincy"
play(player, quincy, 1000, verbose=True)

# Pour tester différentes profondeurs d’analyse
custom_ai = make_player(5)
play(custom_ai, mrugesh, 1000)
````
