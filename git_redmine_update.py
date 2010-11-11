#### Kevin Postal ###
## kevindpostal@gmail.com
#  Because I am using cpanel... 
#  I have to do some lame tricks to sync my git repo's with redmine...
#  
# 2010
#

import os, re, pwd, sys

def git_redmine_sync():
    path = "/home/redmine/git/"
    files = os.listdir(path)
    test = re.compile(".git$", re.IGNORECASE)
    files = filter(test.search, files)
    if files:
        os.chdir("/home/redmine/git")
        for item in files:
            #yep... we are gonna del the repo and reclone it... *face palm*
            os.system("rm -fr %s/%s" % (path,item))
            os.system("/usr/local/bin/git clone --bare git@github.com:kevinpostal/%s" % (item) )
            
            #Maybe once Mike updates git I won't have to del the fucking repo every time
            #print os.system('/usr/local/bin/git "pull git@github.com:kevinpostal/%s"' % (item) ) 

def main(argv=sys.argv):
    git_redmine_sync()
    
    #Update redmine
    os.system('ruby ~/rails_apps/redmine/script/runner "Repository.fetch_changesets" -e production')
    
    
if __name__ == "__main__":
    #Set userid to Redmine (Git wont run without this)
    uid = pwd.getpwnam('redmine')[2]
    os.setuid(uid)
    main()



