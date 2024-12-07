from copy import deepcopy
import numpy as np

ROW   = 0
COL   = 1
UP    = np.array([-1,  0])
DOWN  = np.array([ 1,  0])
LEFT  = np.array([ 0, -1])
RIGHT = np.array([ 0,  1])

class LabGuard:
  def __init__(self, filename) -> None:
    self._is_looped = False
    self._map = ['!' + line.strip() + '!' for line in open(filename, 'r').readlines()]
    self._map.insert(0, '!' * len(self._map[0]))
    self._map.append(self._map[0])

    self._direction = []
    for _ in range(len(self._map)):
      self._direction.append([np.array([0,  0])] * len(self._map[0]))

    for row_index, row in enumerate(self._map):
      col_index = row.find('^')
      if col_index != -1:
        self.position = np.array([row_index, col_index])
        break
    self.direction = UP
    self._visit_current_position()

  def _visit_current_position(self) -> None:
    if self.is_outside():
      return
    self._direction[self.position[ROW]][self.position[COL]] = self.direction
    self._map[self.position[ROW]] = self._map[self.position[ROW]][:self.position[COL]] + 'X' + \
                                  self._map[self.position[ROW]][self.position[COL]+1:]

  def count_visited(self) -> int:
    return sum([row.count('X') for row in self._map])

  def _get_value_at_position(self, position) -> str:
    return self._map[position[ROW]][position[COL]]

  def is_outside(self) -> bool:
    return self._get_value_at_position(self.position) == '!'

  def is_looped(self) -> bool:
    return self._is_looped

  def _is_wall(self, position) -> bool:
    return self._get_value_at_position(position) == '#'

  def move(self) -> None:
    new_position = self.position + self.direction
    if self._is_wall(new_position):
      if   (self.direction == UP).all():    self.direction = RIGHT
      elif (self.direction == DOWN).all():  self.direction = LEFT
      elif (self.direction == LEFT).all():  self.direction = UP
      elif (self.direction == RIGHT).all(): self.direction = DOWN
    else:
      self.position = new_position
      if (self._direction[self.position[ROW]][self.position[COL]] == self.direction).all():
        self._is_looped = True
      self._visit_current_position()

  def add_wall(self, row, col) -> None:
    self._map[row] = self._map[row][:col] + '#' + self._map[row][col+1:]

def get_nof_visited_positions(filename: str) -> int:
  lab_guard = LabGuard(filename)
  while not lab_guard.is_outside():
    lab_guard.move()

  return lab_guard.count_visited()

def get_nof_possible_obstructions(filename: str) -> int:
  lab_guard = LabGuard(filename)
  loops = 0
  for x in range(1, len(lab_guard._map[0]) - 1):
    for y in range(1, len(lab_guard._map) - 1):
      attempt = deepcopy(lab_guard)
      attempt.add_wall(y, x)

      while not attempt.is_outside() and not attempt.is_looped():
        attempt.move()

      if attempt.is_looped():
        loops += 1

  return loops

def print_map(map: list[str]) -> None:
  for row in map:
    print(row)

def main():
  # Part 1
  result = get_nof_visited_positions('example.txt')
  assert result == 41, f"Expected 41, but was {result}."

  result = get_nof_visited_positions('input.txt')
  print(f"Part 1: Result is {result}")

  # Part 2
  result = get_nof_possible_obstructions('example.txt')
  assert result == 6, f"Expected 6, but was {result}."

  result = get_nof_possible_obstructions('input.txt')
  print(f"Part 1: Result is {result}")

if __name__ == "__main__":
  main()
