import pickle
import pprint

data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('representation of data1 before pickling: ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)
data2 = pickle.loads(data1_string)

print('representation of data2 after restored: ')
pprint.pprint(data2)

print('Are the identities of the two objects SAME? :', (data1 is data2))
print('Are the values of the two objects EQUAL?:', (data1 == data2))