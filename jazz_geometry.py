#!/usr/bin/env python


from math_functions import get_fibonacci_sequence_from_function
from meter import get_meter_notes
from sounds_map import get_sound_id
from midi import get_midi, set_midi_notes

bass = get_sound_id('Acoustic_Bass')
bass = get_sound_id('Finger_Bass')
guitar = get_sound_id('Clean_Electric_Guitar')

def compose():
    """ Compose using multiple melodic lines
    """
    instruments = [bass, guitar]
    n_tracks = len(instruments)
    channels = [i for i in range(len(instruments))]
    midi = get_midi(n_tracks, 108,
                    channels,
                    instruments)

    fib_sample = get_fibonacci_sequence_from_function(10e10)[:16]
    bass_rythm = [1/4., 1/4., 3/16., 1/16.]

    notes_bass = get_meter_notes(bass_rythm, 4./4., fib_sample, 3, 120, shuffle_beats=False)
    set_midi_notes(midi, notes_bass, 4., 0, 0, 1, 10)


    notes_guitar = get_meter_notes([1/8., 1/16.], 4./4., fib_sample, 3, 120, shuffle_beats=False)
    set_midi_notes(midi, notes_guitar, 4., 1, 1, 1, 10)


    midi.write("album/track_2_jazz_geometry.mid")


compose()