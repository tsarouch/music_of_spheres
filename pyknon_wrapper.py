from random import shuffle

import sys
pyknon_lib_path = '/Users/charilaostsarouchas/tsarouch_github/pyknon'
#sys.path.insert(0, pyknon_lib_path)
sys.path.append(pyknon_lib_path)

from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq, Rest

from utilities import get_random_item

def pitch_to_note(pitch):
    """ Return the note of the relevant pitch
    e.g. the pitch 121 corresponds to note 121%12 = 1 (C#)
    :pitch: the quality that makes it possible to judge sounds
    as "higher" and "lower" in the sense associated with musical
    melodies
    """
    return pitch % 12


def get_notes(pitch_sample,
              octave_sample,
              duration_sample,
              volume_sample=120):
    """Return the sequence of notes
    """
    notes = NoteSeq()
    shuffle(pitch_sample)
    for pitch in pitch_sample:
        note = pitch_to_note(pitch)
        octave = get_random_item(octave_sample)
        duration = get_random_item(duration_sample)
        vol = get_random_item(volume_sample)
        # compose the single note now
        # default duration = 1/4.
        # default octave = 5
        notes.append(Note(note, octave, duration, vol))
    return notes
