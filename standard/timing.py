# coding=utf-8
import common.func
def information(edid_table):
	for table in range(38,53,2) :
		print "Standard timing information"
		print ("~~~~standard timing inforamtio # %d" %(table))
		print (" 1.X resolution %d " %(get_x_resolution(edid_table_38 = edid_table[table]) ))
		print (" 2.Aspect ratio %s " %(get_aspect_ratio(edid_table_39 = edid_table[table+1])))
		print (" 3.V Freq =  %d Hz" %( get_v_freq(edid_table_39 = edid_table[table+1])))

	print ("~~~~~~~~~~~~~~~~~~")

def get_x_resolution(edid_table_38):
#divided by 8, less 31 (256–2288 pixels, value 00 is reserved and should not be used)
	if edid_table_38 != 0x01 :
	#Versions prior to 1.3 defined 00 as 1:1.)
		return  (int(common.func.get_data_from_byte(byte = edid_table_38, low_bit = 0, high_bit = 7 ),2)  +31 ) *8
	else:
		return 0
def get_aspect_ratio(edid_table_39):

	if edid_table_39 != 0x1:
	#00 : "16 : 10", #if version is 1.3 00 : "1 : 1"
		asp_ratio = {
			00 : "16 : 10",
			01 : "4 : 3",
			10 : "5 : 4",
			11 : "16 : 9"
		}

		byte1 = int(common.func.get_data_from_byte(byte = edid_table_39,low_bit = 6, high_bit = 7 ))
		return asp_ratio.get(byte1)
	else :
		return  0

def get_v_freq(edid_table_39):
	#less 60Hz ~ 123Hz
	if edid_table_39 != 0x1 :
		return int(common.func.get_data_from_byte(byte = edid_table_39,low_bit = 0, high_bit = 5 ),2)+60
	else:
		return 0
