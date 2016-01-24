# notes.py
# Initializes the Note class
# J. Hassler Thurston
# 27 November 2013 (Adapted from Mathematica code written in 2010/2011)
# Python 2.7.6

# Inspired by https://github.com/cuthbertLab/music21/blob/master/music21/note.py

all_keywords = [
    'type', # note or rest
    'pitch', # the note value
    'rhythm', # Rhythm value of the note. For example, "quarter note" would be 1/4
    'duration', # Amount of time the note is played
    'start_time', # Start time of the note
    'end_time', # End time of the note. Note (no pun intended): some keyword values can be deduced
                # from others, but we include them here so we can specify properties of the note in different ways.
    'dynamic', # dynamic marking for the note (represented as a number). Eg. Fortissimo --> 2
]


class Note:
    def __init__(self, **args):
        self.type = None
        self.pitch = None
        self.rhythm = None
        self.duration = None
        self.start_time = None
        self.end_time = None
        self.dynamic = None

        if 'type' in args:
            self.type = args['type']
        if 'pitch' in args:
            self.pitch = args['pitch']
        if 'rhythm' in args:
            self.rhythm = args['rhythm']
        if 'duration' in args:
            self.duration = args['duration']
        if 'start_time' in args:
            self.start_time = args['start_time']
        if 'end_time' in args:
            self.end_time = args['end_time']
        if 'dynamic' in args:
            self.dynamic = args['dynamic']

    # setters
    def set_type(self, newtype):
        self.type = newtype

    def set_pitch(self, newpitch):
        self.pitch = newpitch

    def set_rhythm(self, newrhythm):
        self.rhythm = newrhythm

    def set_duration(self, newduration):
        self.duration = newduration

    def set_start_time(self, newstarttime):
        self.start_time = newstarttime

    def set_end_time(self, newendtime):
        self.end_time = newendtime

    def set_dynamic(self, newdynamic):
        self.dynamic = newdynamic

# checks to see whether something is a Note object


def isNote(object):
    return isinstance(object, Note)
