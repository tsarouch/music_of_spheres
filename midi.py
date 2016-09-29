import sys
pyknon_lib_path = '/Users/charilaostsarouchas/tsarouch_github/pyknon'
sys.path.append(pyknon_lib_path)
from pyknon.genmidi import Midi


def get_midi(n_tracks, tempo, channels_list, instruments):
    return Midi(n_tracks,
                tempo=108,
                channel=channels_list,
                instrument=instruments)


def set_midi_notes(midi, meter_notes, beat_note_value, track, channel, start_meter, end_meter):
    """ Provides the notes to the midi given the start and meter
    :beat_note_value: e.g. if meter signature is 4/4/ the beat note value is the
        denominator, 4.
    """
    n_meters = end_meter - start_meter
    notes = meter_notes * n_meters
    time_value = (start_meter - 1) * beat_note_value
    midi.seq_notes(notes, track=track, channel=channel, time=time_value)
