from dataclasses import dataclass
import numpy as np

X = 0
Y = 1

DIRECTION = {"<": np.array([-1,  0]),
             ">": np.array([ 1,  0]),
             "^": np.array([ 0, -1]),
             "v": np.array([ 0,  1])}

SIBLING = {"[": DIRECTION[">"],
           "]": DIRECTION["<"]}

@dataclass
class Warehouse:
  _map: list[str]
  moves: list[np.ndarray]
  position: np.ndarray

  def map(self, position: np.ndarray) -> str:
    return self._map[position[Y]][position[X]]

  @property
  def gps_sum(self) -> int:
    gps_sum = 0
    for y, row in enumerate(self._map):
      for x, value in enumerate(row):
        if value == "[":
          gps_sum += y * 100 + x
    return gps_sum

  def run(self) -> None:
    for move in self.moves:
      if self.move(self.position, move) == True:
        self.position += move

  def can_move(self, position: np.ndarray, direction: np.ndarray) -> bool:
    value = self.map(position)
    if value == "#":
      return False

    if value == '.':
      return True

    is_up_down = (direction == DIRECTION["^"]).all() or (direction == DIRECTION["v"]).all()
    has_sibling = self.map(position) in "[]"
    new_position = position + direction

    if self.can_move(new_position, direction) == True:
      if is_up_down and has_sibling:
         return True if self.can_move(new_position + SIBLING[value], direction) == True else False
      else:
        return True

    return False

  def move(self, position: np.ndarray, direction: np.ndarray) -> bool:
    if not self.can_move(position, direction):
      return False

    self.do_movement(position, direction)
    return True

  def do_movement(self, position: np.ndarray, direction: np.ndarray):
    new_position = position + direction
    is_up_down = (direction == DIRECTION["^"]).all() or (direction == DIRECTION["v"]).all()
    next_type = self.map(new_position)
    has_sibling = next_type in "[]"

    if self.map(new_position) != '.':
      self.do_movement(new_position, direction)
      if is_up_down and has_sibling:
        sibling_position = new_position + SIBLING[next_type]
        self.do_movement(sibling_position, direction)

    self._map[new_position[Y]][new_position[X]] = self.map(position)
    self._map[position[Y]][position[X]] = "."

def parse_data(filename) -> Warehouse:
  raw_data = open(filename, 'r').readlines()

  map = []
  moves = []
  move_data = ""

  rebuild = {"O": "[]", "#": "##", "@": "@.", ".": ".."}

  for y, line in enumerate(raw_data):
    if line[0] == "#":
      row = []
      [row.extend(list(rebuild[value])) for value in line.strip()]
      map.append(row)
      x = line.find("@")
      if x  >= 0:
        position = np.array([x * 2, y])
    else:
      move_data += line.strip()

  for move in move_data:
    moves.append(DIRECTION[move])

  return Warehouse(map, moves, position)


def print_map(map: list[str]) -> None:
  for row in map:
    print(''.join(row))


def main():
  warehouse = parse_data('example.txt')
  warehouse.run()

  result = warehouse.gps_sum
  assert result == 9021, f"Expected 9021, but was {result}."

  warehouse = parse_data('input.txt')
  warehouse.run()

  print(f"Part 2: Result is {warehouse.gps_sum}")


if __name__ == "__main__":
  main()
