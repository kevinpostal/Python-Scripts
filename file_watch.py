import os, time
path_to_watch = "/Users/zodiac2832/Desktop/a/"
file_to_watch = "test.txt"
command = ""
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (3)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
    if added[0] == file_to_watch:
        print "123"
        print os.system(command)
    

  before = after
