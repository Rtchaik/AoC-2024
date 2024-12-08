from collections import defaultdict
from itertools import permutations


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file) -> tuple:
  with open(my_file) as f:
    city = [line.strip() for line in f]
    antennas = defaultdict(set)
    for y, line in enumerate(city):
      for x, char in enumerate(line):
        if char != '.':
          antennas[char].add((y, x))
    bounds = [len(city), len(city[0])]
    return antennas, bounds


def coord_sub(a: tuple, b: tuple) -> tuple:
  return a[0] - b[0], a[1] - b[1]


def find_antinodes(data: dict, bounds: list, p2: bool = False) -> set:
  antinodes = set()
  for antennas in data.values():
    for a, b in permutations(antennas, 2):
      while True:
        a, b = b, coord_sub(b, coord_sub(a, b))
        if 0 <= b[0] < bounds[0] and 0 <= b[1] < bounds[1]:
          antinodes.add(b)
          if not p2:
            break
        else:
          break
  return antinodes


def part1(data: tuple) -> int:
  return len(find_antinodes(*data))


def part2(data: tuple) -> int:
  return len(
      find_antinodes(*data, True) | set.union(*data[0].values()))
