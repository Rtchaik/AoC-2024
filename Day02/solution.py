from itertools import pairwise


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file) -> list:
  with open(my_file) as f:
    return [[int(num) for num in line.split()] for line in f]


def is_safe(report: list) -> bool:
  diffs = {x - y for x, y in pairwise(report)}
  return all(diff in [1, 2, 3] for diff in diffs) or all(diff in [-1, -2, -3] for diff in diffs)


def part1(data: list) -> int:
  return sum(is_safe(rep) for rep in data)


def part2(data: list) -> int:
  return sum(any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report))) for report in data)
