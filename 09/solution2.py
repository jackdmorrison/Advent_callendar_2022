from Rope import Rope
f = open("File1.txt")
instructions=[]
rope=Rope(10)
for line in f:
    instructions.append(line)
move = {'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)}
unique_tail_pos = set()
for line in instructions:
    direction, steps = line.split()
    for _ in range(int(steps)):
        rope.move_head(*move[direction])
        unique_tail_pos.add(rope.tail.position())
        #print(rope)
print(len(unique_tail_pos))