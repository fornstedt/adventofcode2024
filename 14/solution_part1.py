from dataclasses import dataclass
import re
import numpy as np

@dataclass
class Robot:
  position: np.ndarray
  velocity: np.ndarray

class Map:
  def __init__(self, robots: list, dimension: np.ndarray) -> None:
    self._robots = robots
    self._dimension = dimension

  def tick(self, nof_ticks: int = 1):
    for _ in range(nof_ticks):
      for robot in self._robots:
        robot.position = (robot.position + robot.velocity) % self._dimension

  @property
  def safety_factor(self) -> int:
    sum = 1
    x_size = self._dimension[0] // 2
    y_size = self._dimension[1] // 2
    sum *= len([robot for robot in self._robots if robot.position[0] < x_size and robot.position[1] < y_size])
    sum *= len([robot for robot in self._robots if robot.position[0] > x_size and robot.position[1] < y_size])
    sum *= len([robot for robot in self._robots if robot.position[0] < x_size and robot.position[1] > y_size])
    sum *= len([robot for robot in self._robots if robot.position[0] > x_size and robot.position[1] > y_size])
    return sum

def get_robots(filename: str) -> list[Robot]:
  raw = open(filename, 'r').read()
  robots = []

  robot_data = re.findall(r'p=(.*),(.*) v=(.*),(.*)', raw, )
  for robot in robot_data:
    robots.append(Robot(np.array([int(robot[0]), int(robot[1])]),
                        np.array([int(robot[2]), int(robot[3])])))

  return robots

def main():
  map = Map(get_robots('example.txt'), np.array([11, 7]))
  map.tick(100)
  result = map.safety_factor
  assert result == 12, f"Expected 12, but was {result}."

  map = Map(get_robots('input.txt'), np.array([101, 103]))
  map.tick(100)
  print(f"Part 1: Result is {map.safety_factor}")

if __name__ == "__main__":
  main()
