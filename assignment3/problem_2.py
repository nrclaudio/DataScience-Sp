import MapReduce
import sys
import itertools

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
  # key: table primary key
  # value: list of attributes including table name
  key = record[1]
  value = record[0:]
  mr.emit_intermediate(key, value)


def unpackRelation(relation):
  res = []
  for i in itertools.chain(*relation):
    res.append(i)
  return res


def reducer(key, list_of_values):
  # key: primary key
  # list_of_values: list of attributes including table name
  cross_product = list(itertools.combinations(list_of_values, 2)) # Generate all combinations of elements in list_of_values form [(a,b), (a,c)...] where a, b, c... n are lists of attributes
  for rel in cross_product:
    if rel[0][0] == 'order':
       mr.emit((unpackRelation(rel)))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
