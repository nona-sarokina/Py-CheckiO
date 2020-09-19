def sun_angle(time):
    split = time.split(":")
    hours = int(split[0])
    minutes = int(split[1])
    total_minutes = hours * 60 + minutes
    if 6 * 60 > total_minutes or total_minutes > 18 * 60:
        return "I don't see the sun!"

    return (hours - 6) * 15 + minutes / 4


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
