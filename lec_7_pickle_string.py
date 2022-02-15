import pickle
import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print("original python dictionary object:")
pprint.pprint(data)

data_string = pickle.dumps(data)
print("serialized object as byte string:")
print('{!r}'.format(data_string))