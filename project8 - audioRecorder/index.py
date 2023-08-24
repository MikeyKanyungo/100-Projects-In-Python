import pyaudio
import wave

CHUNK = 1024 #This sets the size of the audio chunk
FORMAT = pyaudio.paInt16 #setting the audio format
CHANNELS = 1 #number of audio channels (1 for mono)
RATE = 44100 #sampling rate measured per second
record_seconds = 5 #sets the duration of the recording in seconds
output_filename = "output.wav" #name of the output file


#initialize the audio stream
p = pyaudio.PyAudio()

#open the audio stream for recording
stream  = p.open(format=FORMAT, 
                 channels=CHANNELS, 
                 rate=RATE,
                 input=True,
                 frames_per_buffer=CHUNK)
print ("Recording ...") #Shows recording status

frames = [] #added frames list to store audio data

for _ in range(0, int(RATE/CHUNK * record_seconds)):
    data = stream.read(CHUNK)
    frames.append(data) #appending the recording data to frames

print ("recording has finished.")

#close and terminate the audio stream
stream.stop_stream()
stream.close()
p.terminate()

#saving the recorded audio to a WAV file
with wave.open(output_filename, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)
    #wf.setsampwidth(p.get_sample_size(format)) 
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))


print(f"audio saved as '{output_filename}'")