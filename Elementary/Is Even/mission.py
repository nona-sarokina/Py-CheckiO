def is_even(num: int) -> bool:
    # your code here
    return num % 2 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
