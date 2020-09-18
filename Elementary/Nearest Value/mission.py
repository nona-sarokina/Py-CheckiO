def nearest_value(values: set, one: int) -> int:
    # your code here
    sorted_list = sorted(values)
    if sorted_list[0] > one:
        return sorted_list[0]
    if sorted_list[-1] < one:
        return sorted_list[-1]

    for i in range(0, len(values) - 1):
        if sorted_list[i] <= one <= sorted_list[i + 1]:
            d1 = one - sorted_list[i]
            d2 = sorted_list[i + 1] - one
            return sorted_list[i] if (d1 <= d2) else sorted_list[i + 1]

    return one


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
