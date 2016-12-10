import os
DATA_DIR = "file/"
file_data = []
for filename in os.listdir(DATA_DIR):
    print "Loading: %s" % filename
    loadFile = open(os.path.join(DATA_DIR, filename), 'r')
    #loadFile.seek(17,0)
    a = loadFile.read()
    #print a
    #print "----"
    count = 0
    for b in a.split('\r\n'):
#	print b
	c = a.split('\r\n')[count]
	print  c.split('  ')[0] + '{0:>10s}'.format(c.split('  ')[1]) + '{0:>10s}'.format(c.split('  ')[2]) + '{0:>10s}'.format(c.split('  ')[3]) + '{0:>10s}'.format(c.split('  ')[4]) + '{0:>10s}'.format(c.split('  ')[5])
	count=count+1

    loadFile.close()

    #loadFile = open(os.path.join(DATA_DIR, filename), 'w')
    #loadFile.write(a)
    #loadFile.close()

