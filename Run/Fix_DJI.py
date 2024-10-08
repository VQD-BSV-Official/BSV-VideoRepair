# Find 00 00 02 & 2Byte NAL - offset
def checkVideo(data):
	offset = data.find(b"\x00\x00\x00\x02")
	print("Found 0x00000002", hex(offset))

	print(hex(offset + 10))
	offset_2Second4Bytes = offset + 10
	nal2Bytes = data[offset + len(b"\x00\x00\x00\x02"):offset + len(b"\x00\x00\x00\x02") + 2]

	return nal2Bytes, offset_2Second4Bytes

# Read 8 byte 'ftyp'
def check8Bytes(File_in):
	with open(File_in, "rb") as r:
		First8Bytes = r.read(8) 

		if b"ftyp" in First8Bytes:
			print("Have ftyp")

# Write 00 00 01
def StartCode(File_out):
	with open(File_out, "ab") as w:
		w.write(b"\x00\x00\x00\x01")

# Write Byte
def writeBytes(byte, File_out):
	"""Write a single byte to the given file."""
	with open(File_out, "ab") as w:
		w.write(bytes([byte]))

#////////////////////NAL_Unit\\\\\\\\\\\\\\\\\\\\
'''def Byte_3337. Read the next 12 bytes and check if there is a 00. 
If there is, replace the next 3 bytes with 00 00 01.'''
def Byte_3337(data):
	count = 0
	while True:
		# Find byte 08 24
		hex_str = bytes.fromhex('0824680000030001')
		offset = data.find(hex_str, count)

		# Break if haven't
		if offset == -1:
			break

		#============main==============
		start = offset + len(hex_str)
		end = start + 12
		# Read 12 byte
		next12Bytes = data[start:end]

		# Find 00 and replace 00 00 01 
		for index, byte in enumerate(next12Bytes):
			if byte == 0:
				print(f"Found byte {byte} at offset {hex(start + index)}")

				replace = start + index + 1
				if replace >= offset + len(hex_str):
					data[replace:replace + 3] = bytes.fromhex('000001')
				break

		count = offset + len(hex_str) + 12

	with open("DJI_FIX.h264", "ab") as w:
		w.write(data)
	# return data

'''def Byte_010209. Read the next 50 bytes and check if there is 0824680000030001.
If there is, replace 00 02 09 with 00 01 09 and skip the next 2 bytes
and replace those 3 bytes with 00 00 01. '''
def Byte_010209(data_in):
	# Read file
	data = bytearray(data_in)
	count = 0
	while True:
		# Find byte 00 02 09
		hex_str = bytes.fromhex('000209')
		hex_check = bytes.fromhex('0824680000030001')
		offset = data.find(hex_str, count)
		
		# Break if haven't
		if offset == -1:
			break

		#============main==============
		start = offset + len(hex_str)
		end = start + 50
		# Read 50 byte
		next50Bytes = data[start:end]

		if hex_check in next50Bytes:
			print(f"Found byte at offset {hex(offset)}")

			data[offset:offset + 3] = bytes.fromhex('000109')
			data[offset + 5:offset + 8] = bytes.fromhex('000001')
		count = offset + len(hex_str) + 50
	
	Byte_3337(data)
#//////////////////////Done\\\\\\\\\\\\\\\\\\\\\\

#//////////////////////MAIN\\\\\\\\\\\\\\\\\\\\\\
def main(File_in, File_out):
	data_in = open(File_in, "rb")

	# Read 8 byte 'ftyp'
	check8Bytes(File_in)

	# x2160 30FPS
	sps = [
		0x27, 0x64, 0x00, 0x33, 0xac, 0x34, 0xc8, 0x03,
		0xc0, 0x04, 0x3e, 0xc0, 0x5a, 0x80, 0x80, 0x80,
		0xa0, 0x00, 0x00, 0x7d, 0x20, 0x00, 0x1d, 0x4c,
		0x1d, 0x0c, 0x00, 0x07, 0x27, 0x08, 0x00, 0x01,
		0xc9, 0xc3, 0x97, 0x79, 0x71, 0xa1, 0x80, 0x00,
		0xe4, 0xe1, 0x00, 0x00, 0x39, 0x38, 0x72, 0xef,
		0x2e, 0x1f, 0x08, 0x84, 0x53, 0x80, 0xfe
	]

	# PPS_Inspire
	pps = [0x28, 0xee, 0x38, 0x30, 0xfe]

	# Write 00 00 01 & header sps
	StartCode(File_out)
	for byte in sps:
		if byte == 0xfe:
			break
		writeBytes(byte, File_out)

	# Write 00 00 01 & header pps
	StartCode(File_out)
	for byte2 in pps:
		if byte2 == 0xfe:
			break
		writeBytes(byte2, File_out)

	# Write 00 00 01 & 2Byte NAL - offset
	StartCode(File_out)
	nal2Bytes, offset_2Second4Bytes = checkVideo(data_in.read(150))
	with open(File_out, "ab") as w:
		w.write(nal2Bytes)

	StartCode(File_out)	
	with open(File_in, "rb") as r:
		test = r.read()

	done_data = Byte_010209(test[offset_2Second4Bytes:])
	# with open(File_out, "ab") as w:
	# 	w.write(done_data)


# main("DJI_BAD.MP4", "DJI_FIX.h264")