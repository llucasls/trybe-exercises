def score(numbers):
    try:
        result = max(numbers) - min(numbers)
    except ValueError:
        result = 0
    return result


def bluff(players):
    player1, player2 = list(players.keys())
    player1_set = set(players[player1])
    player2_set = set(players[player2])
    player1_score = score(player1_set - player2_set)
    player2_score = score(player2_set - player1_set)
    if player1_score > player2_score:
        return player1
    elif player2_score > player1_score:
        return player2
    else:
        return "empate"
