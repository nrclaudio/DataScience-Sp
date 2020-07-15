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
  trimmed_dna = record[1][:-10]
  mr.emit_intermediate(trimmed_dna, 1)


def reducer(key, list_of_values):
  # key: friendship owenr
  # list_of_values: list of friends
  # total: number of friends for each key
  mr.emit(key)



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
