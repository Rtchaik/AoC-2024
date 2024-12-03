import re
from operator import mul


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file) -> list:
  with open(my_file) as f:
    res = re.findall(r"(do\(\)|don\'t\(\)|mul\(\d+,\d+\))", f.read())
    return [(instr if instr.startswith('do') else
             [int(num) for num in re.findall(r'\d+', instr)]) for instr in res]


def part1(data: list) -> int:
  return sum(mul(*instr) for instr in data if isinstance(instr, list))


def part2(data: list) -> int:
  coef = True
  total = 0
  for instr in data:
    match instr:
      case 'do()':
        coef = True
      case 'don\'t()':
        coef = False
      case _:
        total += mul(*instr) * coef
  return total
