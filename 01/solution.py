def calculate_distance(data: list) -> int:
    """Sort the lists, calculate distance and sum the values"""

    list_1 = [int(x[0]) for x in data]
    list_1.sort()

    list_2 = [int(x[1]) for x in data]
    list_2.sort()

    total_distance = sum([abs(x[1]-x[0]) for x in zip(list_1, list_2)])

    return total_distance

def calculate_apperence(data: list) -> int:
    """Multiply each value in list 1 with number of occurences in list 2"""

    list_1 = [int(x[0]) for x in data]
    list_2 = [int(x[1]) for x in data]

    sum_of_ids = sum([x * list_2.count(x) for x in list_1])

    return sum_of_ids

def main():
    # Get data
    example_data = [value_pair.split() for value_pair in open('example.txt', 'r').readlines()]
    real_data = [value_pair.split() for value_pair in open('input.txt', 'r').readlines()]

    # Part 1
    example_distance = calculate_distance(example_data)
    assert example_distance == 11

    distance = calculate_distance(real_data)
    print(f"Part 1: Distance between lists is {distance}")

    # Part 2
    example_apperence = calculate_apperence(example_data)
    assert example_apperence == 31

    apperences = calculate_apperence(real_data)
    print(f"Part 2: Apperences of numbers are {apperences}")


if __name__ == "__main__":
    main()
