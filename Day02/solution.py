from operator import sub


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file) -> list:
  with open(my_file) as f:
    return [[int(num) for num in line.split()] for line in f]


def is_safe(report: list) -> bool:
  diffs = [sub(*pair) for pair in zip(report, report[1:])]
  return all(diff in [1, 2, 3] for diff in diffs) or all(diff in [-1, -2, -3] for diff in diffs)


def part1(data: list) -> int:
  return sum(is_safe(rep) for rep in data)


def part2(data: list) -> int:
  levels = lambda report: any(is_safe(rep) for rep in ([report] + [report[:i-1]+report[i:] for i in range(1, len(report)+1)]))
  return sum(levels(rep) for rep in data)
