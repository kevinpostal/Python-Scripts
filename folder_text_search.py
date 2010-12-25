#
## Kevin Postal ###
## kevindpostal@gmail.com
# This code searches a path and all its subdirectories
# for a string/regular expression then vists the url
#
# 2010
# 

from urlparse import urlparse
import fileinput, glob, string, sys, os, re
from os.path import join

buffsize = 5242880 * 10 #50 Megabyte buffer limit (Server was not having max size)
search_string = r'AKIAIUO7JNJMWSC3V2AA' #search string

def search(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            root = "%s%s" % (path,file_path)
            f = open(file_path, 'r')
            reg_check = re.findall(search_string, f.read(buffsize),re.DOTALL)
            if ( reg_check ):
                site_url = file_path.split("/")[3]
                file_list = list(file_path.split("/")[5:])
                file_path = '/'.join(file_list)
                print root
            f.close()

def main(argv=sys.argv):
    search( argv[1] )

if __name__ == "__main__":
    main()