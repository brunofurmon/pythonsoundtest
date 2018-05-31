import math  # import needed modules

from pyaudiowrapper import PyAudioWrapper
from notes import Notes

bitrate = 48000
channels = 1

A5_1 = Notes.A(5, .25, bitrate)
A5_2 = Notes.A(5, .5, bitrate)

B5_1 = Notes.B(5, .25, bitrate)
B5_2 = Notes.B(5, .5, bitrate)

Bb4_1 = Notes.Bb(4, .25, bitrate)
Bb4_2 = Notes.Bb(4, .5, bitrate)

G4_1 = Notes.G(4, .25, bitrate)
G4_2 = Notes.G(4, .5, bitrate)

C5_1 = Notes.C(5, .25, bitrate)
C5_2 = Notes.C(5, .5, bitrate)

Ab4_1 = Notes.Ab(4, .25, bitrate)
Ab4_2 = Notes.Ab(4, .5, bitrate)

Eb4_1 = Notes.Eb(4, .25, bitrate)
Eb4_2 = Notes.Eb(4, .5, bitrate)

F4_1 = Notes.F(4, .25, bitrate)
F4_8 = Notes.F(4, 2, bitrate)

F6_1_12 = Notes.F(6, .25/3, bitrate)

silence1 = Notes.silence(0.5, bitrate)
silence2 = Notes.silence(0.25, bitrate)

# Let the madness commence
with PyAudioWrapper(channels, bitrate, True) as paudio:
    paudio.writeData(C5_1)
    paudio.writeData(Bb4_1)
    paudio.writeData(C5_2)

    paudio.writeData(Bb4_1)
    paudio.writeData(Ab4_1)
    paudio.writeData(Bb4_2)

    paudio.writeData(Ab4_1)
    paudio.writeData(G4_1)
    paudio.writeData(Ab4_2)

    paudio.writeData(F4_1)
    paudio.writeData(Eb4_1)
    paudio.writeData(F4_8)

    # blblbl
    for _ in range(12):
        paudio.writeData(F6_1_12)

    paudio.writeData(C5_1)
    paudio.writeData(Bb4_1)
    paudio.writeData(C5_2)
