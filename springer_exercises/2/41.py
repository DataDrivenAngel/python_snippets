# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed
# previously.
# Once you have your program working correctly for the notes listed previously you
# should add support for all of the notes from C0 to C8. While this could be done by
# adding many additional cases to your if statement, such a solution is cumbersome,
# inelegant and unacceptable for the purposes of this exercise. Instead, you should
# exploit the relationship between notes in adjacent octaves. In particular, the frequency
# of any note in octave n is half the frequency of the corresponding note in octave n +1.
# By using this relationship, you should be able to add support for the additional notes
# without adding additional cases to your if statement.

notes = {
    "C4" : 261.63,
    "D4" : 293.66,
    "E4" : 329.63,
    "F4" : 349.23,
    "G4" : 392.00,
    "A4" : 440.00,
    "B4" : 493.88
}

note = "C5"

if note in notes:
    print(f"{note} = {notes[note]} Hz")
else:
    octave = note[0]+'4'
    freq = notes[octave] / (2 ** (4-int(note[1])))
    print(f"{note} = {freq} Hz")