import re
import numpy as np
from itertools import combinations

class AntennaMap:
  def __init__(self, filename: str, any_position: bool = False) -> None:
    # Read map
    self.map = [line.strip() for line in open(filename, 'r').readlines()]
    self.width = len(self.map[0])
    self.height = len(self.map)

    # Find antenna types
    antenna_types = set()
    for row in self.map:
      antenna_types.update(re.findall(r'[aA0-zZ9]', row))

    # Find positions for all antenna types
    self.antennas = {}
    for antenna_type in antenna_types:
      positions = []
      for y, row in enumerate(self.map):
        x_positions = [a.start() for a in re.finditer(antenna_type, row)]
        for x in x_positions:
          positions.append(np.array([x, y]))
      self.antennas[antenna_type] = positions

    # Find position of antinodes
    for _, nodes in self.antennas.items():
      antinodes = []
      antenna_pairs = combinations(nodes, 2)

      for antenna_pair in antenna_pairs:
        diff = antenna_pair[0] - antenna_pair[1]
        node_1 = antenna_pair[0] + diff
        node_2 = antenna_pair[1] - diff
        antinodes.append(node_1)
        antinodes.append(node_2)
        if any_position:
          antinodes.append(antenna_pair[0])
          antinodes.append(antenna_pair[1])
          while not self.is_outside(node_1):
            node_1 = node_1 + diff
            antinodes.append(node_1)
          while not self.is_outside(node_2):
            node_2 = node_2 - diff
            antinodes.append(node_2)

      # Filter out outsiders
      for antinode in antinodes:
        if not self.is_outside(antinode):
          self.mark_node(antinode)

  def is_outside(self, node) -> bool:
    return not (0 <= node[0] < self.width and 0 <= node[1] < self.height)

  def mark_node(self, node):
    self.map[node[1]] = self.map[node[1]][:node[0]] + '#' + self.map[node[1]][node[0]+1:]

  def count_antinodes(self) -> int:
    return sum([row.count('#') for row in self.map])

def print_map(map: list[str]) -> None:
  for row in map:
    print(row)

def main():
  example_map = AntennaMap('example.txt')
  real_map = AntennaMap('input.txt')

  # Part 1
  result = example_map.count_antinodes()
  assert result == 14, f"Expected 14, but was {result}."

  result = real_map.count_antinodes()
  print(f"Part 1: Result is {result}")

  example_map = AntennaMap('example.txt', any_position=True)
  real_map = AntennaMap('input.txt', any_position=True)

  # Part 2
  result = example_map.count_antinodes()
  assert result == 34, f"Expected 34, but was {result}."

  result = real_map.count_antinodes()
  print(f"Part 2: Result is {result}")

if __name__ == "__main__":
  main()
