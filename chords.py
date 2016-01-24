from listFunctions import cumulativeSumZero


def getPitches(intervals):
    return cumulativeSumZero(intervals)


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
