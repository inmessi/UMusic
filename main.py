# Print all the notes present in a particular scale

li = [
    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
]

m = int(input("Press 1 for Major scale and 2 for Minor scale: "))

notes = []
inp = input()
root = 0
for i in range(len(li)): 
    if inp == li[i]:
        root = i
        break

i = root if m == 1 else root + 3
if i > len(li) - 1: 
    i = i - len(li)

notes += [li[i]]
for j in range(0, 2):
    i = i + 2
    if i >= len(li):
        i -= len(li)
    notes += [li[i]]
i = i + 1
if i >= len(li):
    i -= len(li)
notes += [li[i]]
    
for j in range(0, 3):
    i = i + 2
    if i >= len(li):
        i -= len(li)
    notes += [li[i]]
i = i + 1
if i >= len(li):
    i -= len(li)
notes += [li[i]]

if (m == 1):
    print (f"The keys under {inp} major scale are: ", end = " ")
else:
    print (f"The keys under {inp} minor scale are: ", end = " ")

print (notes)

# M-m-m-M-M-m-Dim-M
i = 0
print (f"The chords under this scale are: {notes[i]}, {notes[i+1]}m, {notes[i+2]}m, {notes[i+3]}, {notes[i+4]}, {notes[i+5]}m, {notes[i+6]}Dim.")
