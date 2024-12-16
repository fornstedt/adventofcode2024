import re
from sympy import symbols, Eq, solve

def read_machines(filename: str) -> list[dict]:
  machines = []
  raw = open(filename, 'r').read()

  machine_data = re.findall(r'A.*\+(\d+).*\+(\d+)\n.*B.*\+(\d+).*\+(\d+)\n.*=(\d+).*=(\d+)', raw)
  for machine in machine_data:
    machines.append({"AX": int(machine[0]), "AY": int(machine[1]), "BX": int(machine[2]), "BY": int(machine[3]),
                     "PX": int(machine[4]) + 10000000000000, "PY": int(machine[5]) + 10000000000000, "cost": 0})

  return machines


def solve_machine(machine: dict) -> None:
  a, b = symbols('a b')
  eq1 = Eq(a * machine["AX"] + b * machine["BX"], machine["PX"])
  eq2 = Eq(a * machine["AY"] + b * machine["BY"], machine["PY"])
  solution = solve((eq1, eq2), (a, b))

  if solution[a].is_Integer and solution[b].is_Integer:
    cost = solution[a] * 3 + solution[b]
    if cost < machine["cost"] or machine["cost"] == 0:
      machine["cost"] = cost


def main():
  machines = read_machines('input.txt')

  for machine in machines:
    solve_machine(machine)

  result = sum(machine["cost"] for machine in machines)
  print(f"Part 3: Result is {result}")


if __name__ == "__main__":
  main()
