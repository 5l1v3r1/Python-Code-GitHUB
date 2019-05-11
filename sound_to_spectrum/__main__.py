import pyaudio
import numpy as np
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation

RATE = 44100
CHUNK = 8192  # int(RATE/20) # RATE / number of updates per second

fig = plt.figure()
graph_out = fig.add_subplot(2, 1, 1)
fft_out = fig.add_subplot(2, 1, 2)
data = 0


def soundplot(in_data, frame_count, time_info, flag):
    global data
    data = in_data  # np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(data)


def animate(i):
    global data
    data = 2 * np.fromstring(stream.read(CHUNK), dtype=np.int16)
    graph_out.clear()
    graph_out.set_ylim(top=3000, bottom=-3000)
    graph_out.plot(data)
    fft_out.clear()
    fft_data = np.fft.rfft(data)
    fft_data = fft_data[1:round(len(fft_data)/2)]
    fft_data = np.absolute(fft_data)
    maxval = np.amax(fft_data)
    fft_data = fft_data / maxval
    fft_out.plot(fft_data[1:512])


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
time.sleep(0.1)
stream.stop_stream()
stream.close()
p.terminate()
