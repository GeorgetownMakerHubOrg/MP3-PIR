"""
	Protocol definition files for the CATALEX Open-Smart Serial MP3 Player A
	The board uses the QJ004-16S MP3 audio chip.
	This is a subset of those commands:
	
	Command format:
	
	4 byte commands:
	Pos		Description 	Bytes	Value
	0 		Start			1		0x7E
	1		Length			1		0x04 or 0x06
	2		Command			1		see below
	3-4		Feedback		2		command dependent
	4		End				1		0xEF

	# 5 byte commands

	Pos		Description 	Bytes	Value
	0 		Start			1		0x7E
	1		Length			1		0x04 or 0x06
	2		Command			1		see below
	3		Argument		1		command dependent
	4		End				1		0xEF


	6 byte commands:
	Pos		Description 	Bytes	Value
	0 		Start			1		0x7E
	1		Length			1		0x04 or 0x06
	2		Command			1		see below
	3-4		Feedback		2		command dependent
	5		End				1		0xEF
	
	Code 	Commands
	0x01	Resume playback
	0x02	Playback pause
	0x03	Next song
	0x04	Previous song
	0x05	Volume up by 1
	0x06	Volume down by 1
	0x0A	Fast forward
	0x0B 	Fast rewind
	0x0E	Stop play
	0x0F	Stop injecting the song
	0x31	Set volume and play song
	0x35	Reset chip
	0x41	Play song
	0x42	Play song in directory byte 3
	0x0E	Pause playback
	0x0F	Play song in directory provided in byte 5
	0x16	Stop playback
			
"""

def four_byte_command_base():
	command=bytearray()
	command.append(0x7e)
	command.append(0x02)
	command.append(0x00)
	command.append(0xEF)
	return command

def five_byte_command_base():
	command=bytearray()
	command.append(0x7e)
	command.append(0x03)
	command.append(0x00)
	command.append(0x00)
	command.append(0xEF)
	return command

def six_byte_command_base():
	command=bytearray()
	command.append(0x7e)
	command.append(0x04)
	command.append(0x00)
	command.append(0x00)
	command.append(0x00)
	command.append(0xEF)
	return command

# 4 byte commands

def resume():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x01
	return command

def pause():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x02
	return command	

def play_next():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x03
	return command

def play_previous():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x04
	return command
	
def volume_up():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x05
	return command

def volume_down():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x06
	return command
	
def stop():
	command=bytearray()
	command=four_byte_command_base()
	command[2]=0x0E
	return command

# 5 byte commands

def set_volume(level):
	command=bytearray()
	command=five_byte_command_base()
	command[2]=0x31
	command[3]=level
	return command

def reset_module():
	command=bytearray()
	command=five_byte_command_base()
	command[2]=0x35
	command[3]=0x05
	return command

# 6 byte commands

def play_track(track_id):
	command=bytearray()
	command=six_byte_command_base()
	command[2]=0x41
	command[4]=track_id
	return command

def play_volume_track(volume, track_id):
	command=bytearray()
	command=six_byte_command_base()
	command[2]=0x33
	command[5]=volume
	command[6]=track_id	
	return command

def play_directory_track(directory, track_id):
	command=bytearray()
	command=six_byte_command_base()
	command[2]=0x42
	command[3]=directory
	command[4]=track_id	
	return command


