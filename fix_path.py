import string
import os

path = '_posts/'
files = os.listdir(path)
for infile in files:
    print "current file is: " + infile

    updated_file = ''
    with open(path+infile,'rb') as f:
        updated_file = f.read().replace('{{ site.baseurl }}/', '{{ site.baseurl }}')
    with open(path+infile,'wb') as f:
        f.write(updated_file)
