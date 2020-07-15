import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
  # key: friendship owner
  # value: friends with
  key = frozenset(record)
  mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
  # key: friendship owenr
  # list_of_values: list of friends
  # total: number of friends for each key
  total = 0
  for v in list_of_values:
    total += v
  if total < 2:
    friend1, friend2 = key
    mr.emit((friend1, friend2))
    mr.emit((friend2, friend1))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
