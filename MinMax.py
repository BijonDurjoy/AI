MAX = 10000
MIN = -10000
terminal = []


def minimax(depht, nodeIndex, maxPlayer, terminal, alpha, beta):
    if depht == 3:
        return terminal[nodeIndex]
    if maxPlayer:
        move = MIN

        for i in range(0, 2):
            val = minimax(depht + 1, nodeIndex * 2 + i, False, terminal, alpha, beta)
            move = max(move, val)
            alpha = max(alpha, move)

            if beta <= alpha:
                break

            return move

    else:
        move = MAX

        for i in range(0, 2):
            val = minimax(depht + 1, nodeIndex * 2 + i, True, terminal, alpha, beta)
            move = min(move, val)
            alpha = min(alpha, move)

            if beta <= alpha:
                break

            return move


if __name__ == "__main__":
    n = int(input("Enter lenght of terminal: "))

    for i in range(0, n):
        x = int(input())
        terminal.append(x)

    print("The optimal value of MiniMax is : ", minimax(0, 0, True, terminal, MIN, MAX))
