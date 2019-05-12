"""
This is an empty file.
It may be used as a starting point for other tasks.
This file reads the mic input and outputs the data unchanged.
"""

import pyaudio  # pyaudio to record and play audio
import numpy as np  # numpy to do math with the data efficiently


CHUNK = 2048  # samples per iteration
CHANNELS = 1  # 1 channel = mono | 22 channels = stereo
RATE = 44100  # usual 44100Hz sampling frequency


def manipulate_stream(data_in):
    """
    This function will get the input data and manipulate it in some way.
    """

    # do stuff here
    data_out = data_in

    # return the manipulated data
    return np.array(data_out)


# initialize pyaudio
p = pyaudio.PyAudio()


# this is the audio in/out stream with the previously defined parameters
# input and output is set to true to enable recording and playback
stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)


# when this text appers, the program is running
# and therefore done with initializing
print("* recording")

# we catch the keyboard interrupt to exit the stream safely
try:
    while True:
        # read the newest chunk as a numpy array
        data_int = np.fromstring(stream.read(CHUNK), dtype=np.float32)

        # manipulated data here
        new_data = manipulate_stream(data_int)

        # play the manipulated audio
        stream.write(new_data, CHUNK)
except KeyboardInterrupt:
    # this is the safe exit
    # every unexpected interrupt will not raise this message but still exit safely
    print("* keyboard interrupt")

# the stream will now exit
print("* closing")

# first stop stream, then close it
stream.stop_stream()
stream.close()

# terminate the pyaudio object
p.terminate()

print("* terminated completly")
