"""
This is an empty file.
It may be used as a starting point for other tasks.
This file reads the mic input and outputs the data unchanged.
"""

import pyaudio  # pyaudio to record and play audio
import numpy as np  # numpy to do math with the data efficiently


CHUNK_SIZE = 2048  # samples per iteration
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
P_AUDIO = pyaudio.PyAudio()


# this is the audio in/out stream with the previously defined parameters
# input and output is set to true to enable recording and playback
AUDIO_STREAM = P_AUDIO.open(format=pyaudio.paFloat32,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            output=True,
                            frames_per_buffer=CHUNK_SIZE)


# when this text appers, the program is running
# and therefore done with initializing
print("* recording")

# we catch the keyboard interrupt to exit the stream safely
try:
    while True:
        # read the newest chunk as a numpy array
        DATA_IN = np.fromstring(
            AUDIO_STREAM.read(CHUNK_SIZE), dtype=np.float32)

        # manipulated data here
        DATA_OUT = manipulate_stream(DATA_IN)

        # play the manipulated audio
        AUDIO_STREAM.write(DATA_OUT, CHUNK_SIZE)
except KeyboardInterrupt:
    # this is the safe exit
    # every unexpected interrupt will not raise this message but still exit safely
    print("* keyboard interrupt")

# the stream will now exit
print("* closing")

# first stop stream, then close it
AUDIO_STREAM.stop_stream()
AUDIO_STREAM.close()

# terminate the pyaudio object
P_AUDIO.terminate()

print("* terminated completly")
