import math


class Notes(object):

    @classmethod
    def Ab(cls, scale, duration, bitrate):
        return cls.__note__(51.9131, scale, duration, bitrate)

    @classmethod
    def A(cls, scale, duration, bitrate):
        return cls.__note__(55, scale, duration, bitrate)

    @classmethod
    def Bb(cls, scale, duration, bitrate):
        return cls.__note__(58.2705, scale, duration, bitrate)

    @classmethod
    def B(cls, scale, duration, bitrate):
        return cls.__note__(61.7354, scale, duration, bitrate)

    @classmethod
    def C(cls, scale, duration, bitrate):
        return cls.__note__(32.7032, scale, duration, bitrate)
    
    @classmethod
    def D(cls, scale, duration, bitrate):
        return cls.__note__(36.7081, scale, duration, bitrate)

    @classmethod
    def Eb(cls, scale, duration, bitrate):
        return cls.__note__(38.8909, scale, duration, bitrate)

    @classmethod
    def E(cls, scale, duration, bitrate):
        return cls.__note__(41.2034, scale, duration, bitrate)

    @classmethod
    def F(cls, scale, duration, bitrate):
        return cls.__note__(43.6535, scale, duration, bitrate)

    @classmethod
    def G(cls, scale, duration, bitrate):
        return cls.__note__(48.9994, scale, duration, bitrate)

    @staticmethod
    def silence(duration, bitrate):
        totalFrames = int(duration * bitrate)
        wavedata = ''.join([ chr(128) for _ in range(totalFrames) ])
        return wavedata

    @classmethod
    def __note__(cls, basefrequency, scale, duration, bitrate):
        if scale > 6 or scale < 1:
            raise Exception(
                "Scale must be between 1 and 6. Was passed {}".format(scale))

        freq = basefrequency * (2**scale)
        totalframes = int(bitrate * duration)

        # generating waves
        wavedata =''.join([ chr(int(math.sin(x/((bitrate/freq)/math.pi))*127+128)) for x in range(totalframes)])

        return wavedata
