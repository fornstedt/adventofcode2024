from dataclasses import dataclass
from itertools import permutations, product
from operator import add, mul

@dataclass
class Equation:
  result: int
  elements: list[int]


def get_equations(filename: str) -> list[Equation]:
  equations = []
  data_lines = open(filename, 'r').readlines()

  for data in data_lines:
    parts = data.split()
    equations.append(Equation(int(parts[0][:-1]), [int(x) for x in parts[1:]]))

  return equations


def sum_valid(eqations: list[Equation], operators) -> int:
  sum = 0
  for equation in eqations:
    if is_valid(equation, operators):
      sum += equation.result
  return sum


def is_valid(equation: Equation, operators) -> bool:
  operator_combinations = product(operators, repeat=len(equation.elements) - 1)

  for operator_set in operator_combinations:
    result = equation.elements[0]

    for i, op in enumerate(operator_set):
      if isinstance(op, str):
        result = int(str(result) + str(equation.elements[i+1]))
      else:
        result = op(result, equation.elements[i+1])

    if equation.result == result:
      return True

  return False

def main():
  exampel_quations = get_equations('example.txt')
  equations = get_equations('input.txt')

  # Part 1
  result = sum_valid(exampel_quations, [add, mul])
  assert result == 3749, f"Expected 3749, but was {result}."

  result = sum_valid(equations, [add, mul])
  print(f"Part 1: Result is {result}")

  # Part 2
  result = sum_valid(exampel_quations, [add, mul, '||'])
  assert result == 11387, f"Expected 11387, but was {result}."

  result = sum_valid(equations, [add, mul, '||'])
  print(f"Part 2: Result is {result}")

if __name__ == "__main__":
  main()
