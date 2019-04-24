# coding=utf-8
import common.func
def bitmap(edid_table):
	print "Established timing bitmap. Supported bitmap for (formerly) very common timing modes. "
	edid_table_35 = edid_table[35]
	print ("720×400 @ 70 Hz (VGA)  %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 7, high_bit = 7 )))
	print ("720×400 @ 88 Hz (XGA)  %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 6, high_bit = 6 )))
	print ("640×480 @ 60 Hz (VGA)  %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 5, high_bit = 5 )))
	print ("640×480 @ 67 Hz (Apple Macintosh II)   %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 4, high_bit = 4 )))
	print ("640×480 @ 72 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 3, high_bit = 3 )))
	print ("640×480 @ 75 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 2, high_bit = 2 )))
	print ("800×600 @ 56 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 1, high_bit = 1 )))
	print ("800×600 @ 60 Hz   %s" %( common.func.get_data_from_byte(byte = edid_table_35, low_bit = 0, high_bit = 0 )))


	edid_table_36 = edid_table[36]
	print ("800×600 @ 72 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 7, high_bit = 7 )))
	print ("800×600 @ 75 Hz  %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 6, high_bit = 6 )))
	print ("832×624 @ 75 Hz (Apple Macintosh II)   %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 5, high_bit = 5 )))
	print ("1024×768 @ 87 Hz, interlaced (1024×768i)    %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 4, high_bit = 4 )))
	print ("1024×768 @ 60 Hz    %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 3, high_bit = 3 )))
	print ("1024×768 @ 70 Hz    %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 2, high_bit = 2 )))
	print ("1024×768 @ 75 Hz    %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 1, high_bit = 1 )))
	print ("1280×1024 @ 75 Hz    %s" %( common.func.get_data_from_byte(byte = edid_table_36, low_bit = 0, high_bit = 0 )))


	edid_table_37 = edid_table[37]
	print ("1152x870 @ 75 Hz (Apple Macintosh II)   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 7, high_bit = 7 )))
	print ("Other manufacturer-specific display modes bit 6   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 6, high_bit = 6 )))
	print ("Other manufacturer-specific display modes bit 5   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 5, high_bit = 5 )))
	print ("Other manufacturer-specific display modes bit 4   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 4, high_bit = 4 )))
	print ("Other manufacturer-specific display modes bit 3   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 3, high_bit = 3 )))
	print ("Other manufacturer-specific display modes bit 2   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 2, high_bit = 2 )))
	print ("Other manufacturer-specific display modes bit 1   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 1, high_bit = 1 )))
	print ("Other manufacturer-specific display modes bit 0   %s" %( common.func.get_data_from_byte(byte = edid_table_37, low_bit = 0, high_bit = 0 )))
