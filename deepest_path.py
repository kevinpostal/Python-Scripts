import os,sys

list = []
search_path = '/home/'

def nesting(path):
    """ counts how often `os.path.split` works on `path` """
    c = 0
    head = tail = path
    while head and tail:
        head, tail = os.path.split(head)
        c +=1
    return c

def longest_path( paths ):
        return max(paths, key=nesting)

for root, dirs, files in os.walk(search_path):
   for name in files:       
       filename = os.path.join(root, name)
       sys.stdout.write('.')
       list.append(filename)

print longest_path(list)
