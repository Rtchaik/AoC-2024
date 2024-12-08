import Day07.solution as current

test1 = [[190, 10, 19], [3267, 81, 40, 27], [83, 17, 5], [156, 15, 6], [7290, 6, 8, 6, 15], [161011, 16, 10, 13], [192, 17, 8, 14], [21037, 9, 7, 18, 13], [292, 11, 6, 16, 20]]
assert (result:=current.part1(test1))[0] == 3749

assert current.part2(result[1])+result[0] == 11387