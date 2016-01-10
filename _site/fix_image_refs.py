#!/usr/bin/python

#turn:
#<p>[caption id="attachment_203" align="alignleft" width="200"]<img class="size-full wp-image-203" alt="100% Certified!" src="{{ site.baseurl }}assets/works-on-my-machine-starburst1-e1359931607861.png" width="200" height="193" /> 100% Certified![/caption]</p>
#
#to:
#
#<p><figure>
#    <img src='{{ site.baseurl }}assets/works-on-my-machine-starburst1-e1359931607861.png' alt='The Node.js Event Loop Lifecycle' width='200' height='193'/>
#    <figcaption>100% Certified!</figcaption>
#</figure>

import string
import os

path = '_posts/'
files = os.listdir(path)
for infile in files:
    print "Updating image refs in: " + infile

    updated_file = ''
    newlines = []
    #read file
    with open(path+infile,'rb') as f:
        for line in f.readlines():
            # fix if necessary
            if '<img' in line.lower():
                # get necessary values
                width = line.split('width="')[1].split('"')[0]
                height = line.split('height="')[1].split('"')[0]
                alt = line.split('alt="')[1].split('"')[0]
                caption = line.split('/>')[1].split('[')[0].strip()
                imgpath = line.split('src="{{ site.baseurl }}assets/')[1].split('"')[0]

                # write new lines
                newlines.append('<p><figure>')
                newlines.append('<img src=\'{{{{ site.baseurl }}}}assets/{}\' alt=\'{}\' width=\'{}\' height=\'{}\'/>'.format(imgpath, alt, width, height))
                newlines.append('<figcaption>{}</figcaption>'.format(caption))
                newlines.append('</figure>')
            else:
                newlines.append(line)

    with open(path+infile,'wb') as outfile:
        # write updated lines
        for line in newlines:
            outfile.write(line)
