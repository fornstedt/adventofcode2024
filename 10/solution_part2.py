import enum

def calculate_score(map: list[str]):
  start_list = []
  for y, row in enumerate(map):
    start_list.extend([(x, y) for x, pos in enumerate(row) if pos == '0'])

  nines = 0
  for start in start_list:
    nines += find_nines(map, start)

  return nines

def find_nines(map, start) -> int:
  if value_at(map, start) == 9:
    return 1

  nines = 0
  for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    next_pos = (start[0] + dx, start[1] + dy)
    if is_valid(map, start, next_pos):
      nines += find_nines(map, next_pos)

  return nines

def is_valid(map, start, next_pos) -> bool:
  return next_pos[0] >= 0 and next_pos[0] < len(map[0]) and \
         next_pos[1] >= 0 and next_pos[1] < len(map) and \
         (value_at(map,next_pos) - value_at(map,start)) == 1

def value_at(map, pos) -> int:
  return int(map[pos[1]][pos[0]])

def main():
  example_map = [line.strip() for line in open('example.txt', 'r').readlines()]
  map = [line.strip() for line in open('input.txt', 'r').readlines()]

  result = calculate_score(example_map)
  assert result == 81, f"Expected 81, but was {result}."

  result = calculate_score(map)
  print(f"Part 2: Result is {result}")

if __name__ == "__main__":
  main()
