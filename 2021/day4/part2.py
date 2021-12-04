import sys
from board import BingoBoard, BingoBoardWon

with open('input', 'r') as data:
    inputdata = [val.strip() for val in data.readlines()]

chunksize = 6  # 6 lines per board
drawnums = [int(x) for x in inputdata[0].split(',')]
inputdata = inputdata[2:]
chunks = [inputdata[i:i + chunksize - 1] for i in range(0, len(inputdata), chunksize)]

# make boards
boards = []
for chunk in chunks:
    b = BingoBoard(data=chunk)
    b.parse()
    boards.append(b)

# start calling numbers
last_winner = None
for num in drawnums:
    remove = []
    for i in range(len(boards)):
        try:
            b = boards[i]
            b.check(num)
        except BingoBoardWon as bw:
            if len(boards) == 1:
                last_winner = bw
            remove.append(i)  # it won, queue for removal

    # remove won boards
    for i in reversed(remove):
        del boards[i]

print('Last winner remaining sum: {}'.format(last_winner.sum))
print(last_winner.num * last_winner.sum)
