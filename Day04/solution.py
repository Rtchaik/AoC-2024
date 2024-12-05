def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file) -> list:
  with open(my_file) as f:
    return [line.strip() for line in f.readlines()]


def is_valid(data, coord, ch: set) -> bool:
  y, x = coord
  return 0 <= y < len(data) and 0 <= x < len(data[0]) and data[y][x] in ch


def num_of_xmas(data: list, pos: tuple) -> int:
  valid = {
      (pos[0] + y_move, pos[1] + x_move): (y_move, x_move)
      for x_move in (-1, 0, 1)
      for y_move in (-1, 0, 1)
  }
  del valid[(pos[0], pos[1])]
  valid = {k: v for k, v in valid.items() if is_valid(data, k, {'M'})}
  total = 0
  for k, v in valid.items():
    k = [a + b for a, b in zip(k, v)]
    k2 = [a + b for a, b in zip(k, v)]
    total += 1 if (is_valid(data, k, {'A'})
                   and is_valid(data, k2, {'S'})) else 0
  return total


def num_of_mas(data: list, pos: tuple) -> int:
  valid = {
      (pos[0] + y_move, pos[1] + x_move): (y_move, x_move)
      for x_move in (-1, 1)
      for y_move in (-1, 1)
  }
  valid = {k: v for k, v in valid.items() if is_valid(data, k, {'M', 'S'})}
  ms = ''.join(data[pos[0]][pos[1]] for pos in valid)
  return 1 if ms in ('MMSS', 'SSMM', 'MSMS', 'SMSM') else 0


def count_xmas(data: list, ch: str, fun) -> int:
  total = 0
  for y in range(len(data)):
    x = 0
    while (x := data[y].find(ch, x)) != -1:
      total += fun(data, (y, x))
      x += 1
  return total


def part1(data: list) -> int:
  return count_xmas(data, 'X', num_of_xmas)


def part2(data: list) -> int:
  return count_xmas(data, 'A', num_of_mas)
