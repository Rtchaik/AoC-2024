import re
from operator import add, mul


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', (result := part1(data))[0])
  print('Part 2: ', part2(result[1])+result[0])


def parse_data(my_file) -> list:
  with open(my_file) as f:
    return [[int(num) for num in re.findall(r'\d+', line)] for line in f]


def calibration(funcs, result: int, total: int, *args) -> bool:
  if args and (result > total):
    for func in funcs:
      if calibration(funcs, result, func(total, args[0]), *args[1:]):
        return True
    return False
  else:
    return False if args else result == total


def part1(data: list) -> tuple:
  total = 0
  bad_lines = []
  for calib in data:
    if calibration((add, mul), *calib):
      total += calib[0]
    else:
      bad_lines.append(calib)
  return total, bad_lines


def concat(a: int, b: int) -> int:
  return int(str(a) + str(b))


def part2(data: list) -> int:
  return sum(calib[0] for calib in data
             if calibration((add, mul, concat), *calib))
