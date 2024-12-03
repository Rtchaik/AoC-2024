import Day03.solution as current

test1 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

assert current.part1(test1) == 161
assert current.part2(test1) == 48