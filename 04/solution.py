import numpy as np

def count_xmas(matrix: list[str]) -> int:
    sum = 0
    sum += count_back_and_forth(matrix)
    sum += count_back_and_forth(transpose(matrix))
    sum += count_back_and_forth(transpose(skew(matrix)))
    sum += count_back_and_forth(transpose(skew(matrix, left=True)))
    return sum

def count_x_mas(matrix: list[str]) -> int:
    sum = 0
    sum += count_x_mas_shapes(matrix)
    sum += count_x_mas_shapes(transpose(matrix))
    sum += count_x_mas_shapes(transpose(transpose(matrix)))
    sum += count_x_mas_shapes(transpose(transpose(transpose(matrix))))
    return sum

def count_x_mas_shapes(matrix: list[str]) -> int:
    count = 0
    for y in range(0, len(matrix) - 2):
        for x in range(0, len(matrix[0]) - 2):
            if matrix[y    ][x    ] == 'M' and matrix[y  ][x + 2] == 'S' and \
               matrix[y + 1][x + 1] == 'A' and \
               matrix[y + 2][x    ] == 'M' and matrix[y+2][x + 2] == 'S':
                count += 1
    return count

def count_back_and_forth(matrix: list[str]) -> int:
    return sum([line.count('XMAS') + line.count('SAMX') for line in matrix])

def transpose(matrix: list[str]) -> list[str]:
    return [''.join(s)[::-1] for s in zip(*matrix)]

def skew(matrix: list[str], left=False) -> list[str]:
    skewed_matrix = []
    skew_step = 0 if left else len(matrix)
    for line in matrix:
        skewed_matrix.append("." * skew_step + line + "." * (len(matrix) - skew_step))
        skew_step += 1 if left else -1
    return skewed_matrix

def main():
    # Get data
    example_data = [x.strip() for x in open('example.txt', 'r').readlines()]
    real_data = [x.strip() for x in open('input.txt', 'r').readlines()]

    # Part 1
    result = count_xmas(example_data)
    assert result == 18, f"Expected 18, but was {result}."

    result = count_xmas(real_data)
    print(f"Part 1: Result is {result}")

    # Part 2
    result = count_x_mas(example_data)
    assert result == 9, f"Expected 9, but was {result}."

    result = count_x_mas(real_data)
    print(f"Part 2: Result is {result}")

if __name__ == "__main__":
    main()
