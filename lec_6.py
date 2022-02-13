file_object = open('lec_6_pi_digits.txt')
contents = file_object.read()
print(contents)
file_object.close()


with open('lec_6_pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
    

with open('lec_6_pi_digits.txt') as file_object:
    for line in file_object:
        print(line)    


with open('lec_6_pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())



class TrivialIterable:
    def __init__(self, begin=0.0, end=10.0, step=1.0):
        self._begin = begin
        self._end = end
        self._step = step
        self._incr = begin
    def __iter__(self):
        while True:
            if self._incr >= self._end:
                return None
            else:
                yield self._incr
                self._incr += self._step

for i in TrivialIterable(end=5.0):
    print(i)


    
class TrivialIterator:
    def __init__(self, begin=0.0, end=10.0, step=1.0):
        self._begin = begin
        self._end = end
        self._step = step
    def __iter__(self):
        self._incr = self._begin
        return self
    def __next__(self):
        if self._incr >= self._end:
            raise StopIteration
        else:
            ret = self._incr
            self._incr += self._step
            return ret

for i in TrivialIterator(end=5.0):
    print(i)
    
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

from subprocess import check_output
check_output("cat programming.txt", shell=True)

