#!/usr/bin/env python


from math_functions import fibonacci
from pyknon_wrapper import get_notes

import sys
pyknon_lib_path = '/Users/charilaostsarouchas/tsarouch_github/pyknon'
sys.path.append(pyknon_lib_path)
from pyknon.genmidi import Midi


def compose():
    """ Compose using multiple melodic lines
    """

    fib_sample = fibonacci(10e10)[:16]

    N_tracks = 2

    midi = Midi(N_tracks,
                tempo=108,
                channel=[0, 1],
                instrument=[0, 14])


    # motive 1
    notes_1 = get_notes(fib_sample, 1, [1/16., 1/8.], 120) * 4
    midi.seq_notes(notes_1, track=0, channel=0)

    notes_2 = get_notes(fib_sample[:4], 7, [1/16.], 110) * 2
    midi.seq_notes(notes_2, track=1, channel=1, time=3*4)

    notes_2 = get_notes(fib_sample[:4], 7, [1/16.], 110) * 2
    midi.seq_notes(notes_2, track=1, channel=1, time=5*4)

    midi.write("album/fibonacci_spheres.mid")

compose()
