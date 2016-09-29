#!/usr/bin/env python


from math_functions import get_fibonacci_sequence_from_function
from meter import get_meter_notes
from sounds_map import get_sound_id
from midi import get_midi, set_midi_notes


piano = get_sound_id('Acoustic_Grand_Piano')
bells = get_sound_id('Tubular_Bells')
helicopter = get_sound_id('Helicopter')

def compose():
    """ Compose using multiple melodic lines
    """

    fib_sample = get_fibonacci_sequence_from_function(10e10)[:16]

    n_tracks = 3
    midi = get_midi(n_tracks, 108,
                    [0, 1, 2],
                    [piano, bells, helicopter])

    meter_signature = 4/4.

    # piano riff
    notes_1 = get_meter_notes([1/16., 1/8.], 4./4., fib_sample, 1, 120)
    set_midi_notes(midi, notes_1, 4., 0, 0, 1, 10)

    # bells
    notes_2 = get_meter_notes([1/16.], meter_signature, fib_sample, 7, 110, n_beats=6)
    set_midi_notes(midi, notes_2, 4., 1, 1, 2, 3)

    # helicopter appears
    notes_301 = get_meter_notes([4/4.], meter_signature, [1], 5, 100)
    set_midi_notes(midi, notes_301, 4., 2, 2, 3, 4)
    notes_300 = get_meter_notes([4/4.], meter_signature, [1], 5, 110)
    set_midi_notes(midi, notes_300, 4., 2, 2, 4, 5)
    notes_31 = get_meter_notes([4/4.], meter_signature, [1], 5, 100)
    set_midi_notes(midi, notes_31, 4., 2, 2, 5, 6)
    notes_32 = get_meter_notes([4/4.], meter_signature, [1], 5, 80)
    set_midi_notes(midi, notes_32, 4., 2, 2, 6, 7)
    notes_33 = get_meter_notes([4/4.], meter_signature, [1], 5, 60)
    set_midi_notes(midi, notes_33, 4., 2, 2, 7, 8)

    # bells
    notes_4 = get_meter_notes([1/16.], meter_signature, fib_sample, 7, 110, n_beats=6)
    set_midi_notes(midi, notes_4, 4., 1, 1, 7,8)

    midi.write("album/fibonacci_spheres.mid")

compose()
