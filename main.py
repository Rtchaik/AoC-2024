from importlib import import_module
from timeit import default_timer

current_day = "01"  #str(input("Enter day number: ")).zfill(2)
import_module('Day' + current_day + '.tests')
current_module = import_module('Day' + current_day + '.solution')
start_time = default_timer()
current_module.solve_day(f'Day{current_day}/raw.txt')
print(f'Total time: {default_timer() - start_time:.4f}')