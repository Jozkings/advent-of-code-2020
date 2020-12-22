from collections import defaultdict
import copy

FILE_NAME = "input22.in"

players_decks = defaultdict(list)

with open(FILE_NAME, 'r') as file:
    pindex = -1
    for line in file:
        if not line.split():
            continue
        value = line.strip()
        if "Player" in line:
            pindex += 1
            continue
        val = int(value)
        players_decks[pindex].append(val)


def check_finish(players):
    for player in players.keys():
        if not players[player]:
            return True, abs(player - 1)
    return False, None


def turn_quick_into_hashable(players):
    res = ""
    for player, cards in players.items():
        res += str(player) + ":"
        for card in cards:
            res += str(card)
            res += ","
        res += "|"
    return res


def get_result(cards):
    res = 0
    multiplying_by = 1
    for i in range(len(cards) - 1, -1, -1):
        res += multiplying_by * cards[i]
        multiplying_by += 1
    return res


def recursive_combat(players_cards, drawn_cards, level):
    player_1_copy = players_cards[0][:drawn_cards[0]]
    player_2_copy = players_cards[1][:drawn_cards[1]]
    players_copy = defaultdict(list)
    players_copy[0] = player_1_copy
    players_copy[1] = player_2_copy
    player_subcards, sub_winner = play(players_copy, False, level+1)
    return sub_winner


def play(players_cards, first_part, level=1):
    seen = set()
    end_condition, winner = check_finish(players_cards)
    while not end_condition:
        if not first_part:
            decks_stringo = turn_quick_into_hashable(players_cards)
            if decks_stringo in seen:
                return players_cards, 0
            seen.add(decks_stringo)
        drawn_cards = []
        for p, pvalue in players_cards.items():
            drawn_cards.append(pvalue.pop(0))
        if drawn_cards[0] <= len(players_cards[0]) and drawn_cards[1] <= len(players_cards[1]) and not first_part:
            winner = recursive_combat(players_cards, drawn_cards, level)
            players_cards[winner].append(drawn_cards[winner])
            players_cards[winner].append(drawn_cards[abs(winner - 1)])
        else:
            if drawn_cards[0] > drawn_cards[1]:
                players_cards[0].append(drawn_cards[0])
                players_cards[0].append(drawn_cards[1])
            else:
                players_cards[1].append(drawn_cards[1])
                players_cards[1].append(drawn_cards[0])
        end_condition, winner = check_finish(players_cards)
    return players_cards, winner


copy_decks = copy.deepcopy(players_decks)
first_end_decks, first_winner = play(players_decks, True)
print(get_result(first_end_decks[first_winner]))
second_end_decks, second_winner = play(copy_decks, False)
print(get_result(second_end_decks[second_winner]))

