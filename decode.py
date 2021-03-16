def decode():
	print("\nDecoding Starts..")
  #Read the audio file
	audio = wv.open("/content/drive/My Drive/Colab Notebooks/sampleStego.wav", mode='rb')
  # Convert audio to byte array
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
  # Get all LSB's
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
  # divide extracted data into blocks of eight binary strings
  # convert them and join them back to string
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	decoded = string.split("###")[0]
	print("Sucessfully decoded: "+decoded)
	audio.close()	
decode()