from collections import Counter


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return list(zip(*[[int(ch) for ch in line.split()] for line in f.readlines()]))


def part1(data):
  return sum(abs(x-y) for x,y in zip(*[sorted(gr) for gr in data]))


def part2(data):
  c = Counter(data[1])
  return sum(num * c[num] for num in data[0])
