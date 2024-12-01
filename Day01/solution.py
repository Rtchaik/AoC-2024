from operator import sub
from collections import Counter


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return list(
        zip(*[[int(ch) for ch in line.split()] for line in f.readlines()]))


def part1(data):
  return sum(abs(sub(*pair)) for pair in zip(*[sorted(gr) for gr in data]))


def part2(data):
  l0 = Counter(data[0])
  l1 = Counter(data[1])
  return sum(num * l0[num] * l1[num] for num in set(data[0]))
