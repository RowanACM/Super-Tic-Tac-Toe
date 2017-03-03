import sys


class GameState():

    def __init__(self, isxturn, arraygamestate):
        self.xturn = isxturn
        self.gameboard = arraygamestate

    def __str__(selfself):
        pass


class Node():

    def __init__(self, childr, gs, currboard, currplay):
        self.children = childr
        self.gamestate = GameState(True if currplay == "x" else False, gs)
        self.currentboard = currboard
        # currentplayer = currplayer


def minimax(node, depth, maximizingplayer):
    """traverses through possible game states and returns the best move"""
    if depth == 0 or node.children is None:
        return h(node)

    if maximizingplayer:
        bestvalue = -1 - sys.maxint
        for child in node.children:
            v = minimax(child, depth - 1, False)
            bestvalue = v if (v > bestvalue) else bestvalue
        return bestvalue
    else:
        bestvalue = sys.maxint
        for child in node.children:
            v = minimax(child, depth - 1, True)
            bestvalue = v if (v < bestvalue) else bestvalue
        return bestvalue


def h(node):    # heuristic
    h1(node)    # sub-board heuristic
    h2(node)    # super-board heuristic


def h1(node):
    """tries to win subboard"""

    pass


def h2(node):
    """considers the superboard"""
    pass


if __name__ == "__main__":  # example input
    args = sys.argv         # 5 [000000000] [000000000] [000000000] [000000000]
    print("scripting now")  #   [000000000] [100000000] [000000000] [000000000] [000000000]
    print(args)
    currentBoard = args[1]
    boards = [[args[3], args[4], args[5]], [args[6], args[7], args[8]], [args[9], args[10], args[11]]]

    # Make args useful here
    # minimax()
