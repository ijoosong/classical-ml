import pysynth
from MusicMatrix import MusicMatrix

musicLearner = MusicMatrix()
random_score = []
current_note = ["c", 4]
for i in range(0, 100):
    print current_note[0] + ", " + str(current_note[1])
    current_note = musicLearner.next_note(current_note)
    random_score.append(current_note)

pysynth.make_wav(random_score, fn="result.wav")
