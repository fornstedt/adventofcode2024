from dataclasses import dataclass
import numpy as np

X = 0
Y = 1

@dataclass
class Warehouse:
  map: list[str]
  moves: list[np.ndarray]
  position: np.ndarray

  @property
  def gps_sum(self) -> int:
    gps_sum = 0
    for y, row in enumerate(self.map):
      for x, value in enumerate(row):
        if value == "O":
          gps_sum += y * 100 + x
    return gps_sum

  def run(self) -> None:
    for move in self.moves:
      if self.move(self.position, move) == True:
        self.position += move

  def move(self, position: np.ndarray, direction: np.ndarray) -> bool:
    if self.map[position[Y]][position[X]] == "#":
      return False

    new_position = position + direction
    if self.map[new_position[Y]][new_position[X]] == "." or \
       self.move(new_position, direction) == True:
      self.map[new_position[Y]][new_position[X]] = self.map[position[Y]][position[X]]
      self.map[position[Y]][position[X]] = "."
      return True

    return False

def parse_data(filename) -> Warehouse:
  raw_data = open(filename, 'r').readlines()

  map = []
  moves = []
  move_data = ""
  conversion = {"<": np.array([-1,  0]),
                ">": np.array([ 1,  0]),
                "^": np.array([ 0, -1]),
                "v": np.array([ 0,  1])}

  for y, line in enumerate(raw_data):
    if line[0] == "#":
      map.append(list(line.strip()))
      x = line.find("@")
      if x  >= 0:
        position = np.array([x, y])
    else:
      move_data += line.strip()

  for move in move_data:
    moves.append(conversion[move])

  return Warehouse(map, moves, position)


def main():
  warehouse = parse_data('example.txt')
  warehouse.run()

  result = warehouse.gps_sum
  assert result == 10092, f"Expected 10092, but was {result}."

  warehouse = parse_data('input.txt')
  warehouse.run()

  print(f"Part 1: Result is {warehouse.gps_sum}")


if __name__ == "__main__":
  main()
