import os
import boto
import boto.s3 as s3
from time import time

AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
bucket_name = 'foo-bucket_name'

FOLDER_1= 'da_folder1'
FOLDER_2 = 'da_folder2'

##########################
start_time = time()

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
files = conn.get_bucket(bucket_name)

list1 = [ os.path.splitext(os.path.split(item.name)[-1])[0] for item in files.list(prefix=FOLDER_1)  ] 
print "List 1 (%s files) - Created" % len(list1)

list2 = [ os.path.splitext(os.path.split(item.name)[-1])[0] for item in files.list(prefix=FOLDER_2)  ] 
print "List 2 (%s files) - Created" % len(list2)

print "Finding Differences..."
diff_list = [item for item in list1 if not item in list2]

print "Time elapsed: %f" % (time() - start_time)

for item in diff_list: print item
