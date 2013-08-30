


import shutil
import os
pip_list_filename="pip_list.txt"

try:
    shutil.rmtree('robot-indices')
    print 'old robot-indices dir removed'
except:
    print 'robot-indices dir not found.  nothing to cleanup.'

print "creating robot-indices directory"
os.mkdir("robot-indices")

modules = [
           "Selenium2Library",
           "Rammbock",
           "AndroidLibrary",
           "HttpLibrary",
           "RequestsLibrary",           
           ]

for module in modules:
    os.system("python -m robot.libdoc %s list > robot-indices/%s.index"     %   (module,module))
    











# print "creating pip list file"
# os.system("pip list > %s"  %   pip_list_filename)
# print "pip list file created"
# 
# f = open(pip_list_filename, 'r')
# for line in f:
#     print "sssss %s" %  line
# print "cleaning up pip list file"
# os.remove(pip_list_filename)