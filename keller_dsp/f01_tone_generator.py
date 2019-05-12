"""
This is an empty file.
It may be used as a starting point for other tasks.
This file reads the mic input and outputs the data unchanged.
Use Ctrl-C to quit the program safely.
"""

import pyaudio
import numpy as np


# initialize pyaudio
CHUNK_SIZE = 2048  # samples per iteration
CHANNELS = 1       # 1 channel = mono | 2 channels = stereo
RATE = 44100       # sampling frequency in Hz
P_AUDIO = pyaudio.PyAudio()
AUDIO_STREAM = P_AUDIO.open(format=pyaudio.paFloat32,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            output=True,
                            frames_per_buffer=CHUNK_SIZE)


def manipulate_stream(data_in):
    """
    This function will get the input data and manipulate it in some way.
    """

    data_out = data_in

    # return the manipulated data
    return np.array(data_out)


print("running")

# we catch the keyboard interrupt to exit the stream safely
try:
    while True:
        # get data, manipulate, then output
        DATA_IN = np.fromstring(
            AUDIO_STREAM.read(CHUNK_SIZE), dtype=np.float32)
        DATA_OUT = manipulate_stream(DATA_IN)
        AUDIO_STREAM.write(DATA_OUT, CHUNK_SIZE)
except KeyboardInterrupt:
    print("keyboard interrupt")
finally:
    # stop, close and terminate
    AUDIO_STREAM.stop_stream()
    AUDIO_STREAM.close()
    P_AUDIO.terminate()
    print("terminated completly")
