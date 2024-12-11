def blink(stones: list[str]) -> list[str]:
  new_stones = []
  for stone in stones:
    if stone == '0': new_stones.append('1')
    elif len(stone) % 2 == 0: new_stones.extend([stone[:len(stone)//2], str(int(stone[len(stone)//2:]))])
    else: new_stones.append(str(int(stone) * 2024))

  return new_stones

def main():
  stones = open('input.txt', 'r').readline().split()

  for _ in range(25):
    stones = blink(stones)

  print(f"Part 1: Result is {len(stones)}")

if __name__ == "__main__":
  main()
