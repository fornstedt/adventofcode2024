def extract(disk_data: list) -> list:
  disk_list = []

  for i, x in enumerate(disk_data):
    disk_list.extend([(-1 if i % 2 != 0 else i // 2)] * int(x))

  return disk_list


def defrag(disk_data: list) -> list:
  for i in (i for i, v in enumerate(disk_data) if v == -1):

    while disk_data[-1] == -1:
      disk_data.pop()

    if len(disk_data) <= i:
      break

    disk_data[i] = disk_data.pop()

  return disk_data


def calculate_checksum(disk_data: list) -> int:
  return sum(i * int(v) for i, v in enumerate(disk_data) if v != -1)


def main():
  example_disk = list(open('example.txt', 'r').read().strip())
  disk = list(open('input.txt', 'r').read().strip())

  # Part 1
  result = calculate_checksum(defrag(extract(example_disk)))
  assert result == 1928, f"Expected 1928, but was {result}."

  result = calculate_checksum(defrag(extract(disk)))
  print(f"Part 1: Result is {result}")

if __name__ == "__main__":
  main()
