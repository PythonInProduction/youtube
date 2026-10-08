from collections import namedtuple

Payoff = namedtuple("Payoff", ["entrant", "incumbent"])

game = {
    "player": "entrant",
    "actions": {
        "stay out": Payoff(0, 4),
        "enter": {
            "player": "incumbent",
            "actions": {
                "fight": Payoff(-1, -1),
                "accommodate": Payoff(2, 2),
            },
        },
    },
}

def solve(node):
    if isinstance(node, Payoff):
        return [], node
    player = node["player"]
    best_path, best_payoff = [], None
    for action, branch in node["actions"].items():
        path, payoff = solve(branch)
        if best_payoff is None or getattr(payoff, player) > getattr(best_payoff, player):
            best_path = [(player, action), *path]
            best_payoff = payoff
    return best_path, best_payoff

path, payoff = solve(game)
for player, action in path:
    print(f"{player}: {action}")
print("payoff:", payoff)
