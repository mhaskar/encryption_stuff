#!/usr/bin/python

import hashlib

ufile = raw_input("Please enter file path :")

f = open(ufile,"rb")
for i in f.readlines():
 text = "".join(i)

result = hashlib.md5(text).hexdigest()
print "MD5 Hash is : " + result
