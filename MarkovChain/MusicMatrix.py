from MarkovChain import MarkovChain


class MusicMatrix:

    def __init__(self):
        self._previous_note = None
        self._markovNote = MarkovChain(
            ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"])
        self._timings = MarkovChain([1, 2, 4, 8, 16])
        self._markovChord = MarkovChain(
            ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"])

    def add(self, to_note):
        """Add a path from a note to another note. Re-adding a path between
        notes will increase the associated weight."""
        if(self._previous_note is None):
            self._previous_note = to_note
            return
        from_note = self._previous_note
        self._markovNote.add(from_note[0], to_note[0])
        self._timings.add(from_note[1], to_note[1])
        self._markovChord.add(from_note[2], to_note[2])
        self._previous_note = to_note

    def next_note(self, from_note):
        return [
            self._markovNote.next_value(
                from_note[0]), self._timings.next_value(
                from_note[1]), self._markovChord.next_value(from_note[2])]
