#!/usr/bin/python

import binascii
from termcolor import cprint
#transfer data to binary (ascii to hex) --> (hex to binary).
#generate N blocks of data , every block is 64-bit size.

data = "Hi my name is Mohammad Askar , how are you ?" #ascii text
hexed_data = binascii.hexlify(data) # convert ascii to hex
binary_data = "{0:b}".format(int(hexed_data,16)) #convert hex to binary
#################################### END OF TRANSFERRING DATA TO BINARY ####################################
cprint("Plain Text is : %s"%data,"blue")
print "+" * 60
print "total bits number :%s bits"%len(binary_data)
blocks = len(binary_data) / 64 #calculate main blocks number
from_index = 0 #start blocking from index 0
to_index = 64  #start blocking from index 1
cprint("[+]binary data blocks :","yellow")
for i in range(blocks):	#start blocking
  data = binary_data[from_index:to_index] #split data every 64 bit.
  cprint("\t 64-bit block num{0} is : {1}".format(i+1,data),"green")
  from_index = from_index + 64 #increase start split index
  to_index   = from_index + 64 #increase to split index (final result ends with 64 bit)
last_index = to_index - 64 #decrease last index with 64 bit cause it calculated with increased value from for loop
remaining_bits = binary_data[last_index:len(binary_data)] #binary data from last index to len
remaining_char = 64 - len(remaining_bits) #the padding bits length

remaining_bits_data = str(binary_data[last_index:len(binary_data)]) + "1" * remaining_char #binary data from last index to len

l = len(remaining_bits) #final block remaining bits size.
print "\t 64-bit block numf is : {0}".format(remaining_bits_data)
print "+" * 60
cprint("\t final block length : %s bits"%l,"red")
cprint("\t padding with       : %s bits"%remaining_char,"red")
cprint("\t last data value    : %s"%str(binary_data[last_index:len(binary_data)]),"red")
#print "final block length is {0} padding with {1} to equal 64-bit : {2}".format(l,remaining_char,remaining_bits_data)
#################################### END OF BLOCKING AND PADDING ####################################
