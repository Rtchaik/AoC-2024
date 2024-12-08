import re


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', (result := part1(data))[0])
  print('Part 2: ', part2(result[1]) + result[0])


def parse_data(my_file) -> list:
  with open(my_file) as f:
    return [[int(num) for num in re.findall(r'\d+', line)] for line in f]


def calibration(start: int, end: int, nums: list, p2: bool = False) -> bool:
  if nums and (start > end):
    if calibration(start - nums[-1], end, nums[:-1], p2):
      return True
    if not (mult := divmod(start, nums[-1]))[1]:
      if calibration(mult[0], end, nums[:-1], p2):
        return True
    if p2 and start != nums[-1] and (concat := int(
        str(start).removesuffix(str(nums[-1])))) != start:
      if calibration(concat, end, nums[:-1], p2):
        return True
    return False
  else:
    return False if nums else start == end


def part1(data: list) -> tuple:
  total = 0
  bad_lines = []
  for calib in data:
    if calibration(calib[0], calib[1], calib[2:]):
      total += calib[0]
    else:
      bad_lines.append(calib)
  return total, bad_lines


def part2(data: list) -> int:
  return sum(calib[0] for calib in data
             if calibration(calib[0], calib[1], calib[2:], True))
