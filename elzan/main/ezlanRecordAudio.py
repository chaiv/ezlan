'''
Created on 08.10.2022

@author: vital
'''
import pyaudio
import wave
import os
def getLastNumberFileName():
    l=os.listdir(r'G:\Meine Ablage\ezlan\recordings')
    li=[x.split('.')[0] for x in l]
    lastNumberFileName = 0
    for filename in li:
        filenameNumber = int(filename)
        if(filenameNumber>lastNumberFileName):
            lastNumberFileName = filenameNumber
    return str(lastNumberFileName+1)


chunk = 1024 
sample_format = pyaudio.paInt16 
channels = 1
fs = 22050  
seconds = 7
filename = r'G:\Meine Ablage\ezlan\recordings/'+getLastNumberFileName()+'.wav'

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()





