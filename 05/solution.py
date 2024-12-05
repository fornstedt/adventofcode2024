from collections import defaultdict
from pydoc import doc
from typing import Any

def read_data(filename: str) -> tuple[dict, list[list[int]]]:
  lines   = open(filename, 'r').readlines()
  updates = filter_data(lines, ',')

  rules = defaultdict(list)
  for rule in filter_data(lines, '|'):
    rules[rule[0]].append(rule[1])

  return rules, updates

def filter_data(data: list[str], sep: str) -> list[list[int]]:
  filtered = [x.strip().split(sep) for x in list(filter(lambda k: sep in k, data))]
  filtered = [[int(x) for x in item] for item in filtered]
  return filtered

def check_update(rules: dict, update: list) -> tuple[bool,int,int]:
  for index, page in enumerate(update):
    for rule_page in rules[page]:
      try:
        rule_page_index = update.index(rule_page)
        if index > rule_page_index:
          return False, index, rule_page_index  # Not valid, return invalid indexes immediately
      except ValueError:
        pass  # Page not in update

  return True, 0, 0

def sort_updates(rules: dict, updates: list[list]) -> tuple[list[Any], list[Any]]:
  valid = []
  invalid = []
  for update in updates:
    is_valid, _, _ = check_update(rules, update)
    valid.append(update) if is_valid else invalid.append(update)
  return valid, invalid

def sum_updates(updates) -> int:
  return sum([update[len(update)//2] for update in updates])

def fix_update(rules, update) -> None:
  while 1:
    valid, i1, i2 = check_update(rules, update)
    if not valid:
      update[i1], update[i2] = update[i2], update[i1]  # Swap
    else:
      break

def sum_valid_updates(filename: str) -> int:
  rules, updates = read_data(filename)
  valid_updates, _ = sort_updates(rules, updates)
  return sum_updates(valid_updates)

def fix_and_sum_invalid_updates(filename: str) -> int:
  rules, updates = read_data(filename)
  _, invalid_updates = sort_updates(rules, updates)
  for update in invalid_updates:
    fix_update(rules, update)
  return sum_updates(invalid_updates)

def main():
  # Part 1
  result = sum_valid_updates('example.txt')
  assert result == 143, f"Expected 143, but was {result}."

  result = sum_valid_updates('input.txt')
  print(f"Part 1: Result is {result}")

  # Part 2
  result = fix_and_sum_invalid_updates('example.txt')
  assert result == 123, f"Expected 132, but was {result}."

  result = fix_and_sum_invalid_updates('input.txt')
  print(f"Part 2: Result is {result}")

if __name__ == "__main__":
  main()
