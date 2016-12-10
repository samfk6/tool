import os
DATA_DIR = "123456/"
file_data = []
for filename in os.listdir(DATA_DIR):
    print "Loading: %s" % filename
    loadFile = open(os.path.join(DATA_DIR, filename), 'r')
    loadFile.seek(17,0)
    a = loadFile.read()
    print a
    #print "----"
    ##b = a.split(' ')[1]
    #print b
    loadFile.close()

    loadFile = open(os.path.join(DATA_DIR, filename), 'w')
    loadFile.write(a)
    loadFile.close()

