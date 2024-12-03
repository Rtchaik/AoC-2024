import re
from operator import mul


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file) -> str:
  with open(my_file) as f:
    return f.read()


def part1(data: str) -> int:
  return sum(
      mul(*[int(num) for num in instr])
      for instr in re.findall(r"mul\((\d+),(\d+)\)", data))


def part2(data: str) -> int:
  return sum(part1(valid.split("don't()")[0]) for valid in data.split('do()'))
