import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tones import sin_tone, exp_decay

def notelen(duration):
    """ Returns the fraction of time that a note spans, given the duration
    string:

    r: 1
    b: 1/2
    n: 1/4
    c: 1/8
    s: 1/16
    """
    durations = ['r', 'b', 'n', 'c', 's']
    return 1/2**durations.index(duration)

def make_space(notes, rate=8000):
    duration = sum(map(
        lambda x: notelen(x[1]),
        notes
    ))

    return np.zeros(rate*duration)

NOTES = {
    'C': 440 * 2**(1/12 * -9),
    #
    'D': 440 * 2**(1/12 * -7),
    #
    'E': 440 * 2**(1/12 * -5),
    'F': 440 * 2**(1/12 * -4),
    #
    'G': 440 * 2**(1/12 * -2),
    #
    'A': 440,
    #
    'B': 440 * 2**(1/12 * 2),
    'P': 0,
}

if __name__ == '__main__':
    with open('ode_to_joy.music', 'r') as sheet_music:
        breaks = 0

        headers = {}

        for line in sheet_music:
            if line == '\n':
                breaks += 1
                if breaks == 2:
                    break
                continue

            key, value = list(map(
                lambda x:x.strip().lower(),
                line.split(':')
            ))
            headers[key] = value

        if 'semibreve' in headers:
            headers['semibreve'] = float(headers['semibreve'])
        else:
            headers['semibreve'] = 1.0

        notes = list(map(
            lambda x: x.strip().split(' '),
            filter(
                lambda x: not x.startswith('#'),
                sheet_music
            )
        ))

        RATE    = 8000
        MAX_VOL = 15000
        TONE    = sin_tone

        empty_song = make_space(notes, RATE)

        pointer = 0 # keeps current position in song

        for note, duration in notes:
            duration = int(RATE * notelen(duration))

            freq = NOTES[note]
            if freq != 0:
                for i in range(duration):
                    empty_song[pointer + i] = \
                        MAX_VOL *\
                        TONE(freq, RATE, i) *\
                        exp_decay(RATE, i)
            else:
                for i in range(duration):
                    empty_song[pointer + i] = 0

            pointer += duration

        plt.plot(empty_song)
        plt.show()

        wavfile.write('melody.wav', RATE, np.array(empty_song, dtype=np.int16))
