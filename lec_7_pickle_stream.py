import io, pprint
import pickle
 
class Obj:
    def __init__(self, msg):
        self._msg = msg

    def __call__(self):
        print(f"{self._msg}")

out_s = io.BytesIO() # Simulate a file.
pickle.dump(Obj('first'), out_s)
out_s.flush()
pickle.dump(Obj('second'), out_s)
out_s.flush()

# Set up a readable stream.
in_s = io.BytesIO(out_s.getvalue())
# Read the data.
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        o()