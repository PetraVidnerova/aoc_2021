with open("input4", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


numbers = lines[0].split(",")
numbers = [int(num) for num in numbers]


class Board():
    def __init__(self, lines):
        assert len(lines) == 5
        self.board = []
        for line in lines:
            self.board.append([int(num) for num in line.split(" ") if num])

    def mark(self, number):
        target_line = None
        for i, line in enumerate(self.board):
            if number in line:
                target_line = i
                break
        if target_line is not None:
            self.board[target_line] = [
                x if x != number else None
                for x in self.board[target_line]
            ]

    def winner(self):
        for line in self.board:
            if all([num is None for num in line]):
                return True
        for col in range(5):
            if all([line[col] is None for line in self.board]):
                return True
        return False

    def sumup(self):
        return sum([
            x
            for line in self.board
            for x in line
            if x is not None
        ])
        return 0


lines = [line for line in lines[1:] if line]

assert len(lines) % 5 == 0

boards = []
for i in range(0, len(lines), 5):
    boards.append(
        Board(lines[i:i+5])
    )


winner = []

for number in numbers:
    if len(boards) == 1:
        boards[0].mark(number)
        if boards[0].winner():
            break
        else:
            continue
    for board in boards:
        print(board.board)
    print()
    for i, board in enumerate(boards):
        board.mark(number)
        if board.winner():
            winner.append(i)
    if winner:
        boards = [
            b
            for i, b in enumerate(boards)
            if i not in winner
        ]
        winner = []


sum_ = boards[0].sumup()

print(sum_)
print(number)

print(sum_ * number)
