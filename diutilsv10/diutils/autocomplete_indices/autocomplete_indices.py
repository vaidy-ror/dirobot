


import shutil
import os
pip_list_filename="pip_list.txt"

try:
    shutil.rmtree('robot-indices')
    print 'old indices dir removed'
except:
    print 'no indices dir found'

print "creating pip list file"
os.system("pip list > %s"  %   pip_list_filename)
print "pip list file created"

f = open(pip_list_filename, 'r')
for line in f:
    print "sssss %s" %  line




print "cleaning up pip list file"
os.remove(pip_list_filename)