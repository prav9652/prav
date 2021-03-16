import wave as wv
def encode():
  print("\nEncoding Starts..")
  #Read the audio file
  audio = wv.open("/content/drive/My Drive/Colab Notebooks/opera.wav",mode="rb")
  # Convert audio to byte array
  frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
  string = input("Enter the Message ")
  print(string)
  string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
  #print(string)
  bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
  print(bits)
  for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
  frame_modified = bytes(frame_bytes)
  '''for i in range(0,10):
    print(frame_bytes[i])'''
  newAudio =  wv.open('/content/drive/My Drive/Colab Notebooks/sampleStego.wav', 'wb')
  newAudio.setparams(audio.getparams())
  newAudio.writeframes(frame_modified)
  newAudio.close()
  audio.close()
  print(" |---->succesfully encoded inside sampleStego.wav<------|")
encode()