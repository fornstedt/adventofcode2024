import itertools

X = 0
Y = 1

class Garden:
  def __init__(self, map: list[str]) -> None:
    self._map = map
    self._visited = set()
    self.plots = []

    for y, row in enumerate(self._map):
      for x, plant in enumerate(row):
        plot = GardenPlot(self._map, (x, y), self._visited)
        if plot.area > 0:
          self.plots.append(plot)

  @property
  def price(self) -> int:
    return sum([plot.area * plot.sides for plot in self.plots])

class GardenPlot:
  def __init__(self, map: list[str], start_position: tuple[int, int], visited) -> None:
    self._map = map
    self._visited = visited
    self._plot = {}
    self._perimeter = 0
    self._plant_type = map[start_position[Y]][start_position[X]]
    self._perimeter_parts = set()
    self._calculate_plot(start_position)
    if len(self._plot) > 0:
      self._sides = self._calculate_sides()

  def _calculate_plot(self, start: tuple[int, int]) -> None:
    if not self.is_valid(start):
      return

    if self._map[start[Y]][start[X]] == self._plant_type:
      self._plot[start] = 4
      self._visited.add(start)
      for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        next_pos = (start[X] + dx, start[Y] + dy)
        self._calculate_plot(next_pos)

  def is_valid(self, next_pos) -> bool:
    return next_pos[Y] >= 0 and next_pos[Y] < len(self._map[Y]) and \
           next_pos[X] >= 0 and next_pos[X] < len(self._map) and \
           next_pos not in self._visited

  def _calculate_sides(self) -> int:
    sides = 0
    vertical_side_parts = []
    horizontal_side_parts = []

    for plant in self._plot:
      for dx, dy in [(-1, 0), (1, 0)]:
        next_pos = (plant[X] + dx, plant[Y] + dy)
        if next_pos not in self._plot:
          vertical_side_parts.append((plant[X] + dx * 0.1, plant[Y] + dy))

      for dx, dy in [(0, -1), (0, 1)]:
        next_pos = (plant[X] + dx, plant[Y] + dy)
        if next_pos not in self._plot:
          horizontal_side_parts.append((plant[X] + dx, plant[Y] + dy * 0.1))

    columns = set([pos[X] for pos in vertical_side_parts])
    rows = set([pos[Y] for pos in horizontal_side_parts])

    for column in columns:
      side_parts = [part[Y] for part in vertical_side_parts if part[X] == column]
      side_parts.sort()
      sides += self.nof_gaps(side_parts)

    for row in rows:
      side_parts = [part[X] for part in horizontal_side_parts if part[Y] == row]
      side_parts.sort()
      sides += self.nof_gaps(side_parts)

    return sides

  @staticmethod
  def nof_gaps(coordinates) -> int:
    groups = []
    for _, g in itertools.groupby(enumerate(coordinates), lambda x: x[0]-x[1]):
      groups.append(list(map(lambda x: x[1], g)))
    return len(groups)

  @property
  def area(self) -> int:
    return len(self._plot)

  @property
  def sides(self) -> int:
    return self._sides


def main():
  example_map = [line.strip() for line in open('example.txt', 'r').readlines()]
  map = [line.strip() for line in open('input.txt', 'r').readlines()]

  result = Garden(example_map).price
  assert result == 1206, f"Expected 1206, but was {result}."

  result = Garden(map).price
  print(f"Part 2: Result is {result}")


if __name__ == "__main__":
  main()
