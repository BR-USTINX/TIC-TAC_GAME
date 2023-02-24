from sre_parse import State


def sum(a, b, c):
    return a + b + c


def printBoard(xstate, State):
    zero = ('X' if xstate[0] else ('0' if State[0] else 0))
    one = ('X' if xstate[1] else ('0' if State[1] else 1))
    two = ('X' if xstate[2] else ('0' if State[2] else 2))
    three = ('X' if xstate[3] else ('0' if State[3] else 3))
    four = ('X' if xstate[4] else ('0' if State[4] else 4))
    five = ('X' if xstate[5] else ('0' if State[5] else 5))
    six = ('X' if xstate[6] else ('6' if State[6] else 6))
    seven = ('X' if xstate[7] else ('0' if State[7] else 7))
    eight = ('X' if xstate[8] else ('0' if State[8] else 8))

    print(f"{zero} | {one} | {two} ")
    print(f"--| - |--")
    print(f"{three} | {four} | {five}")
    print(f"--| - |--")
    print(f"{six} | {seven} | {eight}")


def checkwin(xstate, State):
    xwins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]
    for win in xwins:
        if (sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("X wins the match")
            return 1
        if (sum(State[win[0]], State[win[1]], State[win[2]]) == 3):
            print("O wins the match")
            return 0
    return -1


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    State = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to this game")
    while (True):
        printBoard(xstate, State)
        if (turn == 1):
            print("X chance")
            value = int(input("Please enter the value: "))
            xstate[value] = 1
        else:
            print("O chance")
            value = int(input("Please enter the value: "))
            State[value] = 1
            cwin = checkwin(xstate, State)
            if (cwin != -1):
                print("MATCH OVER")
                break
        turn = 1 - turn
