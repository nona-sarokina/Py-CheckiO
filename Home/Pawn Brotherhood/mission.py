def safe_pawns(pawns: set) -> int:
    n = 8
    array = [[0 for x in range(n)] for y in range(n)]
    line = 'abcdefgh'
    for p in pawns:
        i = int(p[1]) - 1
        j = line.index(p[0])
        array[i][j] = 1

    c = 0
    for i in reversed(range(1, n)):
        for j in range(n):
            if array[i][j] == 1:
                if (j >= 1 and array[i - 1][j - 1] == 1) or (j < n - 1 and array[i - 1][j + 1]) == 1:
                    c += 1
    return c


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
