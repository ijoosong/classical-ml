import music21


class MIDIReader(object):

    def __init__(self, filename):
        self.score = music21.converter.parse(filename)
        print self.score
        for item in self.score:
            print item
        self.bass = self.score[-1]
        self.treble = self.score[-2]

    def get_notes(self):
        #add chords
        tk, bk = self.get_key_sig()
        key_sig_adjust = {-7: 1, -6: 6, -5: -1, -4: 4, -3: -3, -2: 2, -1: -5, 0: 0, 1: 5, 2: -2, 3: 3, 4: -4, 5: 1, 6: -6, 7: -1}
        ta, ba = key_sig_adjust[tk], key_sig_adjust[bk]
        t = []
        b = []
        for note in self.treble:
            if type(note) == music21.note.Note:
                t.append(note.transpose(ta))
            elif type(note) == music21.chord.Chord:
                t.append(music21.note.Note(note.root(), duration=note.duration).transpose(ta))
        for note in self.bass:
            if type(note) == music21.note.Note:
                b.append(note.transpose(ba))
            elif type(note) == music21.chord.Chord:
                b.append(music21.note.Note(note.root(), duration=note.duration).transpose(ba))
        return t, b

    def get_key_sig(self):
        return (self.treble.getElementsByClass(music21.key.KeySignature)[0].sharps,
                self.bass.getElementsByClass(music21.key.KeySignature)[0].sharps)

    def get_time_sig(self):
        ts = self.treble.getElementsByClass(music21.meter.TimeSignature)[0]
        bs = self.bass.getElementsByClass(music21.meter.TimeSignature)[0]
        return (ts.beat, ts.denominator), (bs.beat, bs.denominator)
