def openfile():

	from Tkinter import Tk
	import tkFileDialog as filedialog # python 2
	#from tkinter.filedialog import askopenfilename #for python3
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	filename = filedialog.askopenfilename()

	#filename = '/home/hugo/Desktop/READ_EDID/IWB_HDMI_1_EDID_20.bin'


	#return it to main.py
	return read_edid(filename,128)

def bin2hex(data):
	import binascii
	data_b2a = binascii.b2a_hex(data)
	#print "**Binary to Ascii** \n"
	#print data_b2a
	return  data_b2a

def read_edid(filename,length):

	#check file type is txt or bin, the mode is 'rt',  or 'rb'
	#data = open(filename, "r")
	data = open(filename, "rb")
	#check mathrod, is a EDID file ?

	#read first 128 bytes , it's edid standard.

        edid_table = []
	print (" 0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F \r")
	for i in range(length):
	    chunk = data.read(1)
	    if not chunk: break
	    print ("%s" %bin2hex(chunk)),
	    if (((i+1) % 8) ==0) : print (" "),

	    if (((i+1) % 16) == 0)  : print ("\r")
	    #if i % 15  : print "\n" get another answer

	    edid_table.append(bin2hex(chunk))
	data.close()
	print ""
	return edid_table
