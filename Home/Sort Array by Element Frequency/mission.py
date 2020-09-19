def frequency_sort(items):
    # your code here
    ordered = []
    count = {}
    for i in items:
        if i not in ordered:
            count[i] = items.count(i)
            ordered.append(i)

    result = []
    sorted_list = sorted(count.items(), key=lambda key_value: key_value[1], reverse=True)
    for i in sorted_list:
        result += [i[0]] * i[1]
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
