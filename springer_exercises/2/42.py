# In the previous question you converted from note name to frequency. In this question
# you will write a program that reverses that process. Begin by reading a frequency
# from the user. If the frequency is within one Hertz of a value listed in the table in
# the previous question then report the name of the note. Otherwise report that the
# frequency does not correspond to a known note. In this exercise you only need to
# consider the notes listed in the table. There is no need to consider notes from other
# octaves.

notes = {
    "C4" : 261.63,
    "D4" : 293.66,
    "E4" : 329.63,
    "F4" : 349.23,
    "G4" : 392.00,
    "A4" : 440.00,
    "B4" : 493.88
}

freqs = dict([(round(value), key) for key, value in notes.items()])


freq = 263

if freq in freqs:
    print(f"{freq} = {freqs[freq]} ")
elif freq+1 in freqs:
    print(f"{freq} is almost {freq+1} which is {freqs[freq+1]} ")
elif freq-1 in freqs:
    print(f"{freq} is almost {freq-1} which is {freqs[freq-1]} ")

