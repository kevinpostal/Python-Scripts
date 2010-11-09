#### Kevin Postal ###
## kevindpostal@gmail.com
# This code checks to see if redmine is up.. if not it is restarted.
#
# 2010
# 

import os,time,sys
from urllib2 import Request, urlopen, URLError

def check_redmine():
    print checkURL('http://redmine.2theleft.la/')

def restart_rails():
    os.chdir("/home/redmine/rails_apps/redmine")
    os.system('mongrel_rails stop')
    time.sleep(5)
    os.system('mongrel_rails start -p 12001 -d -e production -P log/mongrel.pid')

def checkURL(url):
    req = Request(url)
    try:
        response = urlopen(req)
    except URLError, e:
        restart_rails()

def main(argv=sys.argv):
    check_redmine()
    
if __name__ == "__main__":
    main()

