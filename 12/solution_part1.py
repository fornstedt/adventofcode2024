
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
    return sum([plot.area * plot.perimeter for plot in self.plots])

class GardenPlot:
  def __init__(self, map: list[str], start_position: tuple[int, int], visited) -> None:
    self._map = map
    self._visited = visited
    self._plot = {}
    self._perimeter = 0
    self._plant_type = map[start_position[Y]][start_position[X]]
    self._calculate_plot(start_position)
    self._calculate_fence()

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

  def _calculate_fence(self):
    for plant in self._plot:
      for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        next_pos = (plant[X] + dx, plant[Y] + dy)
        if next_pos in self._plot:
          self._plot[plant] -= 1

    self._perimeter = sum([value for _, value in self._plot.items()])

  @property
  def area(self) -> int:
    return len(self._plot)

  @property
  def perimeter(self) -> int:
    return self._perimeter


def main():
  example_map = [line.strip() for line in open('example.txt', 'r').readlines()]
  map = [line.strip() for line in open('input.txt', 'r').readlines()]

  result = Garden(example_map).price
  assert result == 1930, f"Expected 1930, but was {result}."

  result = Garden(map).price
  print(f"Part 1: Result is {result}")


if __name__ == "__main__":
  main()
