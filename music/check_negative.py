from pychord import Chord, find_chords_from_notes
negative_harmony_map = {
    "C": "G",
    "G": "C",
    "C#":"F#",
    "F#": "C#",
    "Db":"Gb",
    "Gb": "Db",
    "D": "F",
    "F": "D",
    "D#": "E",
    "E": "D#",
    "Eb": "E",
    "E": "Eb",
    "A#": "A",
    "A": "A#",
    "Bb": "A",
    "A": "A#",
    "B": "Ab",
    "Ab": "B",
    "B": "G#",
    "G#": "B"
}
def get_negative_chord(chord):
    c = Chord(chord)
    note_list = c.components()[::-1]
    negative_note_list = []
    for note in note_list:
        if note in negative_harmony_map:
            negative_note_list.append(negative_harmony_map[note])
    d = {
            "original_chord": chord,
            "negative_harmony_chord": str(find_chords_from_notes(negative_note_list)).split(":")[1][:-2]
    }
    return d

