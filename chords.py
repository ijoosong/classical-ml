from listFunctions import cumulativeSumZero


def getPitches(intervals):
    return cumulativeSumZero(intervals)
major = [4, 3, 5]
major7 = [4, 3, 4]
major65 = [3, 4, 1]
major43 = [4, 1, 4]
major42 = [1, 4, 3]
major6 = [3, 5]
major64 = [5, 4, 3]
minor = [3, 4, 5]
minor7 = [3, 4, 3]
minor65 = [4, 3, 2]
minor43 = [3, 2, 3]
minor42 = [2, 3, 4]
minor6 = [4, 5]
dom = major
dom7 = [4, 3, 3]
dom65 = [3, 3, 2]
dom43 = [3, 2, 4]
dom42 = [2, 4, 3]
dom6 = major6
dim = [3, 3, 6]
dimmaj7 = [3, 3, 5]
dimmin7 = [3, 3, 4]
dimfull7 = [3, 3, 3]

chords = {'I': [4, 3, 5], 'I7': [4, 3, 4], 'I6': [3, 5], 'I64': [5, 4, 3], 'I43': [3, 4, 1], 'I42': [4, 1, 4],
          'ii': [3, 4, 5], 'ii7': [3, 4, 3], }

class Major:
    """Chord = major"""
    def __init__(self):
        self.name = "major"
        self.intervals = [4,3,5]
        self.pitches = getPitches(self.intervals)
        
        
class Minor:
    """Chord = minor"""
    def __init__(self):
        self.name = "minor"
        self.intervals = [3,4]
        self.pitches = getPitches(self.intervals)


class Augmented:
    """Chord = augmented"""
    def __init__(self):
        self.name = "augmented"
        self.intervals = [4,4]
        self.pitches = getPitches(self.intervals)


class Diminished:
    """Chord = diminished"""
    def __init__(self):
        self.name = "diminished"
        self.intervals = [3,3]
        self.pitches = getPitches(self.intervals)


class Major7:
    """Chord = major seven"""
    def __init__(self):
        self.name = "major seven"
        self.intervals = [4,3,4]
        self.pitches = getPitches(self.intervals)


class Minor7:
    """Chord = minor seven"""
    def __init__(self):
        self.name = "minor seven"
        self.intervals = [3,4,3]
        self.pitches = getPitches(self.intervals)


class Diminished7:
    """Chord = diminished seven"""
    def __init__(self):
        self.name = "diminished seven"
        self.intervals = [3,3,3]
        self.pitches = getPitches(self.intervals)


class HalfDiminished7:
    """Chord = half-diminished seven"""
    def __init__(self):
        self.name = "half-diminished seven"
        self.intervals = [3,3,4]
        self.pitches = getPitches(self.intervals)


class Dominant7:
    """Chord = dominant seven"""
    def __init__(self):
        self.name = "dominant seven"
        self.intervals = [4,3,3]
        self.pitches = getPitches(self.intervals)
