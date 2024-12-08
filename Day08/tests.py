import Day08.solution as current

test1 = ({'0': {(4, 4), (3, 7), (1, 8), (2, 5)}, 'A': {(8, 8), (5, 6), (9, 9)}}, [12, 12])

assert current.part1(test1) == 14
assert current.part2(test1) == 34
