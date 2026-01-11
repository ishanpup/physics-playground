import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pydub import AudioSegment
import os


file_list = glob.glob("audio_folder/*.wav")#change the name of the file to whatever you would like

Amaxes = []
Fmaxes = []

trial = 0
for file in file_list:
    sampling_rate, data = wavfile.read(file)
    if len(data.shape) > 1: #if stereo audio, then converts to mono (only left)
        data = data[:, 0]
    data = data / np.max(np.abs(data)) #

#
    N = len(data) # number of audio samples
    fft_data = np.fft.fft(data) #convert data to complex numbers
    fft_freq = np.fft.fftfreq(N, d=1/sampling_rate)#converts complex numbers to frequencies

#makes sure that only the positive frequencies are shown
    pos_mask = fft_freq > 0
    fft_freq = fft_freq[pos_mask]
    fft_amplitude = np.abs(fft_data[pos_mask])


    indexmax = np.argmax(fft_amplitude) #finds the time when max amplitude is shown
    Amaxes.append(fft_amplitude[indexmax]) #appends max amplitude
    Fmaxes.append(fft_freq[indexmax]) #appends frequency when amplitude is max
    #why not the max frequency? the goal is the analyze a single moment of sound, and I assume that is the loudest moment in the audio file.
    trial = trial + 1

    print(f" {trial} {round(fft_freq[indexmax],3)} Hz")

    plt.figure(figsize=(10,5))
    plt.plot(fft_freq, fft_amplitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Frequency Spectrum of the Tap")
    plt.xlim(0, 1000)
    plt.grid(True)
    plt.show()




