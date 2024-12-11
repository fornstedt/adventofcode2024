from collections import defaultdict

def blink(stones: dict) -> dict:
  new_stones = defaultdict(int)
  for stone, count in stones.items():
    if stone == '0':
      new_stones['1'] += count
    elif len(stone) % 2 == 0:
      half = len(stone) // 2
      new_stones[stone[half:].lstrip("0") or "0"] += count
      new_stones[stone[:half]] += count
    else:
      new_stones[str(int(stone) * 2024)] += count

  return new_stones

def main():
  stones = defaultdict(int)
  for stone in open('input.txt', 'r').readline().split():
    stones[stone] += 1

  for _ in range(75):
    stones = blink(stones)

  count = sum(value for _, value in stones.items())
  print(f"Part 2: Result is {count}")

if __name__ == "__main__":
  main()
