#coding=utf-8
import common.func
def  descriptor(edid_table):
	for table in range(54,125,18):
		bytes1 = int((common.func.get_data_from_byte(byte= edid_table[table+1], low_bit = 0, high_bit =7)),2)
		bytes0 = int((common.func.get_data_from_byte(byte= edid_table[table+0], low_bit = 0, high_bit =7)),2)
		if((bytes1 != 0) and (bytes0 != 0)):
			print ("Pixel clock  %2.2f Mhz" %(float(bytes1 * 256 + bytes0)/100))
			print ("Horizontal active pixels %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+4], low_bit = 4, high_bit =7)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+2], low_bit = 0,high_bit =7)),2))))
			print ("Horizontal blanking pixels %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+4], low_bit = 0, high_bit =3)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+3], low_bit = 0,high_bit =7)),2))))
			print ("Vertical active pixels %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+7], low_bit = 4, high_bit =7)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+5], low_bit = 0,high_bit =7)),2))))
			print ("Vertical blanking pixels %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+7], low_bit = 0,high_bit =3)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+6], low_bit = 0, high_bit =7)),2))))
			print ("Horizontal front porch %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+11], low_bit = 6, high_bit =7)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+8], low_bit = 0,high_bit =7)),2))))
			print ("Horizontal sync pulse width pixels %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+11], low_bit = 4,high_bit =5)),2) * 256\
									+(int((common.func.get_data_from_byte(byte= edid_table[table+9], low_bit = 0, high_bit =7)),2))))

			print ("Vertical front porch (sync offset) lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+11], low_bit = 2, high_bit =3)),2) * 64\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+10], low_bit = 4, high_bit =7)),2))))
			print ("Vertical sync pulse width lines  %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+11], low_bit = 0, high_bit =1)),2) * 64\
									+(int((common.func.get_data_from_byte(byte= edid_table[table+10], low_bit = 0, high_bit =3)),2))))

			print ("Horizontal image size %d mm" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 4, high_bit =7)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+12], low_bit = 0,high_bit =7)),2))))
			print ("Vertical image size %d mm" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 256\
								+(int((common.func.get_data_from_byte(byte= edid_table[table+13], low_bit = 0,high_bit =7)),2))))
			print ("Horizontal border pixels %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 4, high_bit =7)),2) * 2))
			print ("Vertical border lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 2 ))

			print ("Interlaced %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+17], low_bit = 7, high_bit =7))) ))
			stereo_mode(edid_table, table)
			print ("Vertical border lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 2 ))
			print ("Vertical border lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 2 ))
			print ("Vertical border lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 2 ))
			print ("Vertical border lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 2 ))
			print ("Vertical border lines %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =3)),2) * 2 ))

			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		else:
			edid_other_monitor_descriptors(edid_table, table)

def stereo_mode(edid_table, table):
	if(common.func.get_data_from_byte(byte= edid_table[table+17], low_bit = 5, high_bit =6 ) == 00):
		print "No Stereo Mode"
	elif(common.func.get_data_from_byte(byte= edid_table[table+17], low_bit = 5, high_bit =6 == 00) and (common.func.get_data_from_byte(byte= edid_table[table+17], low_bit = 0) == 0)):
		print "test"


def edid_other_monitor_descriptors(edid_table, table):
	#print ("table %d" %(int((common.func.get_data_from_byte(byte= edid_table[table + 10], low_bit = 0, high_bit =7)),2)))
	if((int((common.func.get_data_from_byte(byte= edid_table[table + 2], low_bit = 0, high_bit =7)),2) !=0) \
	    and (int((common.func.get_data_from_byte(byte= edid_table[table + 4], low_bit = 0, high_bit =7)),2)!= 0)):
		print "edid_other_monitor_descriptors ERROR1"
	table_3 = int((common.func.get_data_from_byte(byte= edid_table[table + 3 ], low_bit = 0, high_bit =7)),2)
	#table+5 ~table+17
	if(table_3 == 0xff):
		#Display serial number (ASCII text)
		print " serial number"
	elif(table_3 == 0xfe):
		#Unspecified text (ASCII text)
		print "Unspecified text (ASCII text)"
	elif(table_3 == 0xfd):
		table_10 = int((common.func.get_data_from_byte(byte= edid_table[table + 10 ], low_bit = 0, high_bit =7)),2)
		table_11 = int((common.func.get_data_from_byte(byte= edid_table[table + 11 ], low_bit = 0, high_bit =7)),2)
		#Display range limits. 6- or 13-byte (with additional timing) binary descriptor.
		if(table_10 == 0x0):
			#Video timing parameters (if byte 10 is 00 or 01, padded with 0A 20 20 20 20 20 20).
			deid_display_range_limits_descriptor(edid_table, table)
		elif(table_10 == 0x1):
			#Video timing parameters (if byte 10 is 00 or 01, padded with 0A 20 20 20 20 20 20).
			print "No timing information."
		elif((table_10 == 0x2) and (table_11 ==0x0)):
			 edid_display_range_limits_with_gtf_secondary_curve(edid_table, table)
		elif(table_10 == 0x4):
			deid_display_range_limits_with_cvt_support(edid_table, tablei)
		else:
			print ("Display range limits ERROR")
	elif(table_3 == 0xfc):
		#Display name (ASCII text).
		print "Display name (ASCII text)."
	elif(table_3 == 0xfb):
		#Additional white point data. 2× 5-byte descriptors, padded with 0A 20 20.
		print "Additional white point data. 2× 5-byte descriptors, padded with 0A 20 20."
	elif(table_3 == 0xfa):
		#Additional standard timing identifiers. 6× 2-byte descriptors, padded with 0A.
		print "Additional standard timing identifiers. 6× 2-byte descriptors, padded with 0A."
	elif(table_3 == 0xf9):
		#Display Color Management (DCM).
		edid_color_management_data_descriptor(edid_table, table)
	elif(table_3 == 0xf8):
		#CVT 3-Byte Timing Codes.
		edid_cvt_3_byte_timing_codes_descriptor(edid_table, table)
	elif(table_3 == 0xf7):
		print "additional standard timing 3."
		edid_additional_standard_timing_v3(edid_table, table)
	elif(table_3 == 0x10):
		#Dummy identifier.
		print "Diummy identifier."
	elif(table_3 == 0x00):
		#00-0x0Fh Manufacturer reserved descriptors.
		print "00-0x0Fh Manufacturer reserved descriptors"
	else:
		print "ERROR2"


def deid_display_range_limits_descriptor(edid_table, table):

	h_r_offset = {
		00 : "0",
		01 : "0",
		10 : "255", #for Max rate,
		11 : "255" #for Max and Min rates 
	}

	tmp =  common.func.get_data_from_byte(byte = edid_table[table + 4], low_bit = 0, high_bit = 1 )
	print ("Minimum vertical field rate   %d" %( int( common.func.get_data_from_byte(byte = edid_table[table + 5], low_bit = 0, high_bit = 7 ),2) + int( tmp)))
	print ("Maximum vertical field rate   %d" %( int( common.func.get_data_from_byte(byte = edid_table[table + 6], low_bit = 0, high_bit = 7 ),2) + int( tmp)))

	tmp =  common.func.get_data_from_byte(byte = edid_table[table + 4], low_bit = 2, high_bit = 3 )
	print ("Minimum horizontal line rate  %d" %( int( common.func.get_data_from_byte(byte = edid_table[table + 7], low_bit = 0, high_bit = 7 ),2) + int( tmp)))
	print ("Maximum horizontal line rate  %d" %( int( common.func.get_data_from_byte(byte = edid_table[table + 8], low_bit = 0, high_bit = 7 ),2) + int( tmp)))

	print ("Maximum pixel clock rate  %d" %( int( common.func.get_data_from_byte(byte = edid_table[table + 9], low_bit = 0, high_bit = 7 ),2*10)))

def edid_display_range_limits_with_gtf_secondary_curve(edid_table, table):
	print "EDID Display Range Limits with GTF Secondary curve"
	print("Start frequency for secondary curve %d  khz" %(int((common.func.get_data_from_byte(byte= edid_table[table+12], low_bit = 0, high_bit =7)),2) * 2 ))
	print("GTF C value %2.2f" %(int((common.func.get_data_from_byte(byte= edid_table[table+13], low_bit = 0, high_bit =7)),2) / 2 ))
	print("GTF M value %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =7)),2) * 256\
				+(int((common.func.get_data_from_byte(byte= edid_table[table+15], low_bit = 0, high_bit =7)),2))))
	print("GTF k value %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+16], low_bit = 0, high_bit =7)),2)))
	print("GTF j value %2.2f" %(int((common.func.get_data_from_byte(byte= edid_table[table+17], low_bit = 0, high_bit =7)),2) / 2 ))

def deid_display_range_limits_with_cvt_support(edid_table, tablei):
	print "EDID Display Range Limits with CVT support"


def edid_additional_white_point_descriptor(edid_table, table):
	point_number = common.func.get_data_from_byte(byte = edid_table[table+5], low_bit = 0, high_bit = 7)
	if(point_number != 0):
		for point_n in range(point_number):
			table = table + 5 * pointi_n
			print("White point index number %d" %(point_n))
			#White point CIE xy coordinates least-significant bits (like EDID byte 26)
			print ("Gamma %f" %(common.func.get_data_from_byte(byte= edid_table[table+9], low_bit = 0, high_bit =7)/100+1))
	else:
		print "Not used."

def edid_color_management_data_descriptor(edid_table, table):
	if(common.func.get_data_from_byte(byte = edid_table[table+5], low_bit = 0, high_bit = 7) == 3):
		print("Read a3 %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+7], low_bit = 0, high_bit =7)),2) * 256\
					+(int((common.func.get_data_from_byte(byte= edid_table[table+6], low_bit = 0, high_bit =7)),2))))
		print("Read a2 %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+9], low_bit = 0, high_bit =7)),2) * 256\
					+(int((common.func.get_data_from_byte(byte= edid_table[table+8], low_bit = 0, high_bit =7)),2))))
		print("Green a3 %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+11], low_bit = 0, high_bit =7)),2) * 256\
					+(int((common.func.get_data_from_byte(byte= edid_table[table+10], low_bit = 0, high_bit =7)),2))))
		print("Green a2 %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+13], low_bit = 0, high_bit =7)),2) * 256\
					+(int((common.func.get_data_from_byte(byte= edid_table[table+12], low_bit = 0, high_bit =7)),2))))
		print("Blue a3 %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+15], low_bit = 0, high_bit =7)),2) * 256\
					+(int((common.func.get_data_from_byte(byte= edid_table[table+14], low_bit = 0, high_bit =7)),2))))
		print("Blue a2 %d" %(int((common.func.get_data_from_byte(byte= edid_table[table+17], low_bit = 0, high_bit =7)),2) * 256\
					+(int((common.func.get_data_from_byte(byte= edid_table[table+16], low_bit = 0, high_bit =7)),2))))
	else:
		print (" edid_color_management_data_descriptor ERROR")

def edid_cvt_3_byte_timing_codes_descriptor(edid_table, table):
	if(common.func.get_data_from_byte(byte = edid_table[table+5], low_bit = 0, high_bit = 7) == 3):
		for layer in range(4):
			cvt_timing_descriptor(edid_table, table , layer)
	else:
		print ("edid_cvt_3_byte_timing_codes_descriptor Error")

def cvt_timing_descriptor(edid_table, table, layer):
	shift = 6 + 3 * layer
	lisb =  common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 0, high_bit = 7 )
	shift = 7 + 3 * layer
	print ("Addressable lines   %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 4, high_bit = 7 )*256 + lisb))
	print ("Preferred vertical rate   %s" %( preferred_vertical_rate(edid_table[table + shift])))
	print ("bit 1-0 unused, must be 0")
	shift = 8 + 3 * layer
	print ("640×350 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 7, high_bit = 7 )))
	print ("Aspect ratio   %s" %(aspect_ratio (edid_table[table + shift])))
	#Vertical rate bitmap 
	print ("50 Hz CVT   %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 4, high_bit = 4 )))
	print ("60 Hz CVT   %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 3, high_bit = 3 )))
	print ("75 Hz CVT  %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 2, high_bit = 2 )))
	print ("85 Hz CVT   %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 1, high_bit = 1 )))
	print ("60 Hz CVT reduced blanking  %s" %( common.func.get_data_from_byte(byte = edid_table[table + shift], low_bit = 0, high_bit = 0 )))

def preferred_vertical_rate(edid_table_shift):
	P_v_r ={
		00:"50Hz",
		01:"60Hz",
		10:"75HZ",
		11:"85Hz"
	}
	return p_v_r.get(common.func.get_data_from_byte(byte = edid_table_shift, low_bit = 2, high_bit = 3 ))
def aspect_ratio(edid_table_shift):
	asp ={
		00:"16:10",
		01:"4:3",
		10:"5:4",
		11:"16:9"
	}
	return asp.get(common.func.get_data_from_byte(byte = edid_table_shift, low_bit = 5, high_bit = 6 ))

def edid_additional_standard_timing_v3(edid_table, table):
	if(common.func.get_data_from_byte(byte = edid_table[table+5], low_bit = 0, high_bit = 7) == 10):
		print ("640×350 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 7, high_bit = 7 )))
		print ("640×400 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 6, high_bit = 6 )))
		print ("720×400 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 5, high_bit = 5 )))
		print ("640×480 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 4, high_bit = 4 )))
		print ("848×480 @ 60 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 3, high_bit = 3 )))
		print ("800×600 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 2, high_bit = 2 )))
		print ("1024×768 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 1, high_bit = 1 )))
		print ("1152×864 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +6], low_bit = 0, high_bit = 0 )))

		print ("1280×768 @ 60 Hz (CVT-RB)  %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 7, high_bit = 7 )))
		print ("1280×768 @ 60 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 6, high_bit = 6 )))
		print ("1280×768 @ 75 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 5, high_bit = 5 )))
		print ("1280×768 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 4, high_bit = 4 )))
		print ("1280×960 @ 60 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 3, high_bit = 3 )))
		print ("1280×960 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 2, high_bit = 2 )))
		print ("1280×1024 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 1, high_bit = 1 )))
		print ("1280×1024 @ 85 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +7], low_bit = 0, high_bit = 0 )))

		print ("1360×768 @ 60 Hz (CVT-RB)  %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 7, high_bit = 7 )))
		print ("1280×768 @ 60 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 6, high_bit = 6 )))
		print ("1440×900 @ 60 Hz (CVT-RB)    %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 5, high_bit = 5 )))
		print ("1440×900 @ 75 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 4, high_bit = 4 )))
		print ("1440×900 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 3, high_bit = 3 )))
		print ("1440×1050 @ 60 Hz (CVT-RB)    %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 2, high_bit = 2 )))
		print ("1440×1050 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 1, high_bit = 1 )))
		print ("1440×1050 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +8], low_bit = 0, high_bit = 0 )))

		print ("1440×1050 @ 85 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 7, high_bit = 7 )))
		print ("1680×1050 @ 60 Hz (CVT-RB)   %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 6, high_bit = 6 )))
		print ("1680×1050 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 5, high_bit = 5 )))
		print ("1680×1050 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 4, high_bit = 4 )))
		print ("1680×1050 @ 85 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 3, high_bit = 3 )))
		print ("1600×1200 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 2, high_bit = 2 )))
		print ("1600×1200 @ 65 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 1, high_bit = 1 )))
		print ("1600×1200 @ 70 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +9], low_bit = 0, high_bit = 0 )))

		print ("1600×1200 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 7, high_bit = 7 )))
		print ("1600×1200 @ 85 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 6, high_bit = 6 )))
		print ("1792×1344 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 5, high_bit = 5 )))
		print ("1792×1344 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 4, high_bit = 4 )))
		print ("1856×1392 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 3, high_bit = 3 )))
		print ("1856×1392 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 2, high_bit = 2 )))
		print ("1920×1200 @ 60 Hz (CVT-RB)  %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 1, high_bit = 1 )))
		print ("1920×1200 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +10], low_bit = 0, high_bit = 0 )))

		print ("1920×1200 @ 65 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 7, high_bit = 7 )))
		print ("1920×1200 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 6, high_bit = 6 )))
		print ("1920×1440 @ 60 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 5, high_bit = 5 )))
		print ("1920×1440 @ 75 Hz %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 4, high_bit = 4 )))
		print ("table +11 bit 3~0 Unused")
		#print ("table +11 bit 3~0 Unused  %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 3, high_bit = 3 )))
		#print ("800×600 @ 85 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 2, high_bit = 2 )))
		#print ("1024×768 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 1, high_bit = 1 )))
		#print ("1152×864 @ 85 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table[table +11], low_bit = 0, high_bit = 0 )))

		print ("table + 12~17 	Unused, must be 0. ")
	else:
		print "ERROR"
