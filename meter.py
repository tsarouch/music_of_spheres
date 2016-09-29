from random import shuffle

import sys
pyknon_lib_path = '/Users/charilaostsarouchas/tsarouch_github/pyknon'
sys.path.append(pyknon_lib_path)

from music_functions import get_beats, pitch_to_note
from utilities import get_random_item

from pyknon.music import Note, NoteSeq, Rest


def get_meter_notes(beats_sample,
                    meter_signature,
                    pitch_sample,
                    octave_sample,
                    volume_sample=120,
                    shuffle_pitch_sample=True,
                    shuffle_beats=True,
                    n_beats=None):

    """ Return the sequence of notes
    """
    notes = NoteSeq()
    # get the beats
    if shuffle_beats:
        beats = get_beats(beats_sample, meter_signature)
    else:
        beats = beats_sample

    if n_beats:
        beats=beats[:n_beats]

    vol = get_random_item(volume_sample)

    for ctr, beat in enumerate(beats):

        if shuffle_pitch_sample:
            pitch = get_random_item(pitch_sample)
        else:
            pitch = pitch_sample[ctr]
        note = pitch_to_note(pitch)
        octave = get_random_item(octave_sample)

        notes.append(Note(note, octave, beat, vol))
    return notes
