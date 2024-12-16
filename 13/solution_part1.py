import re

def read_machines(filename: str) -> list[dict]:
  machines = []
  raw = open(filename, 'r').read()

  machine_data = re.findall(r'A.*\+(\d+).*\+(\d+)\n.*B.*\+(\d+).*\+(\d+)\n.*=(\d+).*=(\d+)', raw)
  for machine in machine_data:
    machines.append({"AX": int(machine[0]), "AY": int(machine[1]), "BX": int(machine[2]), "BY": int(machine[3]),
                     "PX": int(machine[4]), "PY": int(machine[5]), "cost": 0})

  return machines


def solve_machine(machine: dict) -> None:
  for a in range(machine["PX"] // machine["AX"]):
    a_div = divmod(machine["PX"] - a * machine["AX"], machine["BX"])
    if (a_div[1] != 0) and \
       (not (machine["PY"] - a * machine["AY"]) % machine["BY"] == 0):
      continue

    b = a_div[0]
    if machine["AY"] * a + machine["BY"] * b == machine["PY"]:
      cost = a * 3 + b
      if cost < machine["cost"] or machine["cost"] == 0:
        machine["cost"] = cost


def main():
  machines = read_machines('example.txt')

  for machine in machines:
    solve_machine(machine)

  result = sum(machine["cost"] for machine in machines)
  assert result == 480, f"Expected 480, but was {result}."

  machines = read_machines('input.txt')

  for machine in machines:
    solve_machine(machine)

  result = sum(machine["cost"] for machine in machines)
  print(f"Part 1: Result is {result}")


if __name__ == "__main__":
  main()
