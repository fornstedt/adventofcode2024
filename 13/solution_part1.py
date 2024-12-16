import re

def read_machines(filename: str) -> list[dict]:
  machines = []
  raw = open(filename, 'r').read()

  machine_data = re.findall(r'A.*\+(\d+).*\+(\d+)\n.*B.*\+(\d+).*\+(\d+)\n.*=(\d+).*=(\d+)', raw)
  for machine in machine_data:
    machines.append({"AX": machine[0], "AY": machine[1], "BX": machine[2], "BY": machine[3],
                     "PX": machine[4], "PY": machine[5]})

  return machines

def main():
  machines = read_machines('example.txt')

  print(machines)
#   result = Garden(example_map).price
#   assert result == 1930, f"Expected 1930, but was {result}."

#   result = Garden(map).price
#   print(f"Part 1: Result is {result}")


if __name__ == "__main__":
  main()
