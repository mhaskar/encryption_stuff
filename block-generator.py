#!/usr/bin/python

import binascii
from termcolor import cprint
#transfer data to binary (ascii to hex) --> (hex to binary).
#generate N blocks of data , every block is 64-bit size.

data = "Hi my name is Mohammad Askar , how are you ?"
hexed_data = binascii.hexlify(data)
binary_data = "{0:b}".format(int(hexed_data,16))
#################################### END OF TRANSFERRING DATA TO BINARY ####################################
cprint("Plain Text is : %s"%data,"blue")
print "+" * 60
print "total bits number :%s bits"%len(binary_data)
blocks = len(binary_data) / 64
from_index = 0
to_index = 64
cprint("[+]binary data blocks :","yellow")
for i in range(blocks):	
  data = binary_data[from_index:to_index]
  cprint("\t 64-bit block num{0} is : {1}".format(i+1,data),"green")
  from_index = from_index + 64
  to_index   = from_index + 64
last_index = to_index - 64
left_bits = binary_data[last_index:len(binary_data)] #binary data from last index to len
left_char = 64 - len(left_bits)

left_bits_data = str(binary_data[last_index:len(binary_data)]) + "1" * left_char #binary data from last index to len

l = len(left_bits)
print "\t 64-bit block numf is : {0}".format(left_bits_data)
print "+" * 60
cprint("\t final block length : %s bits"%l,"red")
cprint("\t padding with       : %s bits"%left_char,"red")
cprint("\t last data value    : %s"%str(binary_data[last_index:len(binary_data)]),"red")
#print "final block length is {0} padding with {1} to equal 64-bit : {2}".format(l,left_char,left_bits_data)
#################################### END OF BLOCKING AND PADDING ####################################
