from itertools import cycle

def solve_day(my_file):
  data = parse_data(my_file)

  print('Part 1: ', (p1:=part1(*data))[0])
  print('Part 2: ', part2(*data, p1[2]))


def parse_data(my_file) -> tuple:
  with open(my_file) as f:
    lab = [line.strip() for line in f]
    for y, line in enumerate(lab):
      if (x:=line.find('^')) != -1:
        start = (y,x)
        break
    return lab, start


def pos_counter(lab:list, current:tuple, obstacle:tuple = (-1,-1)) -> tuple:
  is_loop = False
  dirs = cycle([(-1,0),(0,1), (1,0), (0,-1)])
  cur_dir = next(dirs)
  visited = {(current,cur_dir)}
  while True:
    new = tuple(a+b for a,b in zip(current, cur_dir))
    if not ((0 <= new[1] < len(lab[0])) and (0 <= new[0] < len(lab))):
      break
    elif (lab[new[0]][new[1]] == '#') or (new == obstacle):
      cur_dir = next(dirs)
    else:
      current = new
    if (current,cur_dir) in visited:
      is_loop = True
      break
    visited.add((current,cur_dir))
  return len({v0 for v0,v1 in visited}), is_loop, {v[0] for v in visited}

def part1(lab:list, current:tuple) -> tuple:
  return pos_counter(lab,current)

def part2(lab:list, current:tuple, obstacles:set) -> int:
  total = 0
  for y,x in (obstacles - {current}):
        total += pos_counter(lab, current, (y,x))[1]
  return total
