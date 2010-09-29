#### Kevin Postal ###
## kevindpostal@gmail.com
# This code searches a path and all its subdirectories
# for a string/regular expression then vists the url
#
# 2010
# 

from httplib import HTTP
from urlparse import urlparse
import fileinput, glob, string, sys, os, re 
from os.path import join

buffsize = 5242880 * 10 #50 Megabyte buffer limit (Server was not having max size)
search_string = r'select.+phone.+agent' #search string

def search(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            f = open(file_path, 'r')
            reg_check = re.findall(search_string, f.read(buffsize),re.DOTALL)
            if ( reg_check ):
                site_url = file_path.split("/")[3] 
                file_list = list(file_path.split("/")[5:])
                file_path = '/'.join(file_list)
                url = "http://%s/%s" % (site_url,file_path)
                print "%s - %s" % (url,checkURL(url) )
            f.close()    

def checkURL(url):
     p = urlparse(url)
     h = HTTP(p[1])
     h.putrequest('HEAD', p[2])
     h.endheaders()
     if h.getreply()[0] == 200: return 1
     else: return 0

    
def main(argv=sys.argv):
    search( argv[1] )
    
if __name__ == "__main__":
    main()

