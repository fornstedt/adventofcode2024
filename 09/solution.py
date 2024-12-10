from copy import deepcopy, copy

DATA = 0
LENGTH = 1
FREE = -1


def extract(disk_data: list) -> list:
  disk_list = []

  for i, x in enumerate(disk_data):
    disk_list.extend([(FREE if i % 2 != 0 else i // 2)] * int(x))

  return disk_list


def defrag_part1(disk_data: list) -> list:
  for i in (i for i, v in enumerate(disk_data) if v == FREE):

    while disk_data[-1] == FREE:
      disk_data.pop()

    if len(disk_data) <= i:
      break

    disk_data[i] = disk_data.pop()

  return disk_data

def defrag_part2(disk_data: list) -> list:
  disk_map = []
  length = 0
  value = disk_data[0]

  # Create map
  for i, v in enumerate(disk_data):
    if v == value:
      length += 1
    else:
      disk_map.append([value, length])
      value = v
      length = 1
  disk_map.append([value, length])

  first_free = 0
  last_file = len(disk_map) - 1

  while last_file > 0:
    # Clear trailing empty space
    while disk_map[last_file][DATA] == FREE:
      last_file -= 1

    # Get first large enough free space
    first_free = 0
    while disk_map[first_free][DATA] != FREE or \
          disk_map[first_free][LENGTH] < disk_map[last_file][LENGTH]:
      first_free += 1
      if first_free >= last_file:
        first_free = -1
        break

    # Move file
    if first_free > 0:
      file = copy(disk_map[last_file])
      disk_map[last_file][DATA] = FREE
      disk_map[first_free][LENGTH] -= file[LENGTH]
      disk_map.insert(first_free, file)
    else:
      last_file -= 1

  # Restructure disk_list
  new_disk = []
  for item in disk_map:
    new_disk.extend([item[DATA]] * item[LENGTH])

  return new_disk


def calculate_checksum(disk_data: list) -> int:
  return sum(i * int(v) for i, v in enumerate(disk_data) if v != FREE)


def main():
  example_disk = list(open('example.txt', 'r').read().strip())
  disk = list(open('input.txt', 'r').read().strip())

  # Part 1
  result = calculate_checksum(defrag_part1(extract(example_disk)))
  assert result == 1928, f"Expected 1928, but was {result}."

  result = calculate_checksum(defrag_part1(extract(disk)))
  print(f"Part 1: Result is {result}")

  example_disk = list(open('example.txt', 'r').read().strip())
  disk = list(open('input.txt', 'r').read().strip())

  # Part 2
  result = calculate_checksum(defrag_part2(extract(example_disk)))
  assert result == 2858, f"Expected 2858, but was {result}."

  result = calculate_checksum(defrag_part2(extract(disk)))
  print(f"Part 2: Result is {result}")

if __name__ == "__main__":
  main()
