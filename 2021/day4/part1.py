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
for num in drawnums:
    for b in boards:
        try:
            b.check(num)
        except BingoBoardWon as bw:
            print(bw)
            print('Board remaining sum: {}'.format(bw.sum))
            print(bw.num * bw.sum)

            sys.exit()  # not in a fn, don't care to make one
