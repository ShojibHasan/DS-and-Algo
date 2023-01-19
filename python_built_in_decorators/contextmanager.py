# @contextmanager: Make a Customized Context Manager
'''
Python has a context manager mechanism to help you manage resources properly.


'''
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print("The file is opening...")
    file = open(filename,mode)
    yield file
    print("The file is closing...")
    file.close()

with file_manager('test.txt', 'w') as f:
    f.write('Yang is writing!')