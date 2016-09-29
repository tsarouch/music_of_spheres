from utilities import get_random_item


def pitch_to_note(pitch):
    """ Return the note of the relevant pitch
    e.g. the pitch 121 corresponds to note 121%12 = 1 (C#)
    :pitch: the quality that makes it possible to judge sounds
    as "higher" and "lower" in the sense associated with musical
    melodies
    """
    return pitch % 12


def get_beats(beats_sample, meter_signature):
    """ Return the beats of a meter signature given a beats sample
    :beats_sample: A list of beats to be used to construct the meter signature
        e.g. [1./16., 1./8.]
    :meter_signature: Notational convention used in Western musical notation
        to specify how many beats (pulses) are to be contained in each bar and
         which note value is to be given one beat. E.g. 4./4.
    """
    beats = []
    total_duration = 0
    while total_duration < meter_signature:
        d = get_random_item(beats_sample)
        total_duration += d
        beats.append(d)
    # correct if the beats duration > meter_signature
    if sum(beats) > meter_signature:
        _ = beats.pop()
        beats.append(meter_signature - sum(beats))
    # correct if the beats duration < meter_signature
    elif sum(beats) < meter_signature:
        beats.append(meter_signature - sum(beats))
    return beats
