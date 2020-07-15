import MapReduce
import sys
from collections import defaultdict
import itertools
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

dim = 5


def mapper(record):
  # record[0]: table identifier
  # record[1]: i
  # record[2]: j
  # record[3]: v

  if record[0] == "a":
    # replicate all the values in a, to all the columns in b
    for i in range(dim):
      key = (record[1], i)
      value = (record[2], record[0], record[3])
      mr.emit_intermediate(key, value)

  elif record[0] == "b":
    # replicate all the values in b to all the rows in a
    for i in range(dim):
      key = (i, record[2])
      value = (record[1], record[0], record[3])
      mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
  values = {}
  for j, t, v in list_of_values:
    values.setdefault(j, []).append(v)

  total = 0
  for k, v in values.items():
    if len(v) != 2:
      total += 0
    elif len(v) == 2:
      total += v[0] * v[1]

  mr.emit((key[0], key[1], total))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
