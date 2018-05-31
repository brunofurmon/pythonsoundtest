import pyaudio  # sudo apt-get install python-pyaudio


class PyAudioWrapper(object):
    def __init__(self, channels, bitrate, output):
        self._pyAudio = pyaudio.PyAudio()
        self.channels = channels
        self.bitrate = bitrate
        self.output = output

    def __enter__(self):
        formatWidth = self._pyAudio.get_format_from_width(1)
        self._stream = self._pyAudio.open(format = formatWidth,
                                          channels = self.channels,
                                          rate = self.bitrate,
                                          output = self.output)
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._stream.stop_stream()
        self._stream.close()
        self._pyAudio.terminate()

    def writeData(self, wavedata):
        self._stream.write(wavedata)
