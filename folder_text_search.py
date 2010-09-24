#### Kevin Postal ###
## kevindpostal@gmail.com
# This code searches a path and all its subdirectories
# for a string/regular expression
#
# 2010
# 


import fileinput, glob, string, sys, os, re 
from os.path import join

buffsize = 5242880 * 10 #50 Megabyte buffer limit (Server was not having 
max size)
search_string = r'select.+phone.+agent' #search string

def search(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            f = open(file_path, 'r')
            reg_check = re.findall(search_string, 
f.read(buffsize),re.DOTALL)
            if ( reg_check ):
                print file_path
            f.close()    


def main(argv=sys.argv):
    search( argv[1] )
    
if __name__ == "__main__":
    main()

