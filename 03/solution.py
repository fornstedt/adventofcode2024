import re

def calculate_muls(data: str) -> int:
    return sum([int(x[0]) * int(x[1]) for x in re.findall(r"mul\((\d+),(\d+)\)", data)])

def calculate_enabled_muls(data: str) -> int:
    result = 0
    for segment in data.split("do()"):
        result += calculate_muls(segment.split("don't()")[0])
    return result

def main():
    # Get data
    example_data = open('example.txt', 'r').read()
    real_data = open('input.txt', 'r').read()

    # Part 1
    result = calculate_muls(example_data)
    assert result == 161, f"Expected 161, but was {result}."

    result = calculate_muls(real_data)
    print(f"Part 1: Result is {result}")

    # Part 2
    result = calculate_enabled_muls(example_data)
    assert result == 48, f"Expected 48, but was {result}."

    result = calculate_enabled_muls(real_data)
    print(f"Part 2: Result is {result}")

if __name__ == "__main__":
    main()
