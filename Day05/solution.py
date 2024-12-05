from collections import defaultdict


def solve_day(my_file):
  data = parse_data(my_file)
  p1 = part1(*data)
  print('Part 1: ', sum(middles(page) for page in p1[1]))
  print('Part 2: ', part2(data[0], p1[0]))


def parse_data(my_file) -> tuple:
  with open(my_file) as f:
    rules, pages = f.read().split('\n\n')
    rules = [tuple(line.split('|')) for line in rules.split()]
    before = defaultdict(set)
    for v, k in rules:
      before[k].add(v)
    pages = [line.split(',') for line in pages.split('\n')]
    return (before, pages)


def middles(manual: list) -> int:
  return int(manual[len(manual) // 2])


def part1(rules: dict, pages: list) -> list:
  correct_or_no = [[], []]
  for manual in pages:
    correct_or_no[all(not (rules.get(page, set()) & set(manual[idx + 1:]))
                      for idx, page in enumerate(manual))].append(manual)
  return correct_or_no


def sorting(pages: list, rules: dict) -> list:
  pages.reverse()
  new = []
  while pages:
    current = pages.pop()
    if (move_up := rules.get(current, set()) & set(pages)):
      for page in move_up:
        pages.remove(page)
      new.extend(sorting(list(move_up), rules))
    new.append(current)
  return new


def part2(rules: dict, pages: list) -> int:
  return sum(middles(sorting(manual, rules)) for manual in pages)
