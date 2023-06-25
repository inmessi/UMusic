# Print all the notes present in a particular scale

li = [
    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
]

inp = input()
root = 0
for i in range(len(li)): 
    if inp == li[i]:
        root = i
        break

i = root
print (li[i], end = ' ')
for j in range(0, 2):
    i = i + 2
    if i >= len(li):
        i -= len(li)
    print (li[i], end = ' ')
    
i = i + 1
if i >= len(li):
    i -= len(li)
print (li[i], end = ' ')

for j in range(0, 3):
    i = i + 2
    if i >= len(li):
        i -= len(li)
    print (li[i], end = ' ')
i = i + 1
if i >= len(li):
    i -= len(li)
print (li[i], end = ' ')


