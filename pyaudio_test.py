import pyaudio
import math
import struct
import wave
import time
import os

FORMAT = pyaudio.paInt16
CHANNELS = 2
SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
RATE = 48000
swidth = 2
noiseGate = 40

TIMEOUT_LENGTH = 2.5

save_directory = os.path.dirname(os.path.abspath(__file__))

class voiceRecorder:

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)
        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=chunk)

    def record(self):
        print('Recording speech...')
        rec = []
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH

        while current <= end:
            data = self.stream.read(chunk)
            if self.rms(data) >= noiseGate: end = time.time() + TIMEOUT_LENGTH

            current = time.time()
            rec.append(data)
        self.saveRecording(b''.join(rec))

    def saveRecording(self, recording):
        recording_name = "s2t_test_recording"

        filename = os.path.join(save_directory, '{}.wav'.format(recording_name))

        sv = wave.open(filename, 'wb')
        sv.setnchannels(CHANNELS)
        sv.setsampwidth(self.p.get_sample_size(FORMAT))
        sv.setframerate(RATE)
        sv.writeframes(recording)
        sv.close()
        print('Recording saved as: {}'.format(filename))

