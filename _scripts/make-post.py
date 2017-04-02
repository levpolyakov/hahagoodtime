import sys
import re

# ls images/comics | xargs -n 1 python _scripts/make-post.py

imageRe = re.compile('^\(\d\d\d\d-\d\d-\d\d\)-(.*)\..*$')
imageRe = re.compile('^(\d\d\d\d-\d\d-\d\d)-(.*)\..*$')

if len(sys.argv) < 2:
    print "Expecting image file name"
    sys.exit(1)

image = sys.argv[1]
m = imageRe.match(image)
if not m:
    print "Image name format must be yyyy-mm-dd-some-description.ext"
    sys.exit(1)
    
date = imageRe.match(image).group(1)
name = imageRe.match(image).group(2)

outFile = "_posts/haha-goodtime/%s-%s.md" % (date, name)
output = open(outFile, 'w')
output.write("""---
layout: panel
title: "%s"
date: %s 18:21:45 -0500
categories: haha-goodtime
---
""" % (name, date))
output.close()
print "Written", outFile
