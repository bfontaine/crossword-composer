import copy

from models.direction import Direction
from models.position import Position
from models.word import Word


class GridBuilder:
    def __init__(self, array2d):
        self.grid = array2d
        self.h = len(array2d)
        self.w = len(array2d[0])
        self.words_list = []

    def build_as_words_list(self):
        for i, val in enumerate(self.grid):
            startP = Position(i, 0)
            endP = Position(i, 0)
            newWord = Word(Direction.Across, startP, endP)
            for j, val1 in enumerate(val):
                if val1 == 0:
                    if newWord.length > 1:
                        newWord = Word(Direction.Across, startP, endP)
                        self.words_list.append(newWord)
                        startP = Position(i, j)
                        endP = Position(i, j)
                        newWord = Word(Direction.Across, startP, endP)
                    startP = Position(i, j + 1)

                else:
                    endP = Position(i, j)
                    newWord = Word(Direction.Across, startP, endP)
            if newWord.length > 1:
                newWord = Word(Direction.Across, startP, endP)
                self.words_list.append(newWord)

        print("--------------------------")

        for j, val in enumerate(zip(*self.grid)):
            startP = Position(0, j)
            endP = Position(0, j)
            newWord = Word(Direction.Down, startP, endP)
            for i, val1 in enumerate(val):
                if val1 == 0:
                    if newWord.length > 1:
                        newWord = Word(Direction.Down, startP, endP)
                        self.words_list.append(newWord)
                        startP = Position(i, j)
                        endP = Position(i, j)
                        newWord = Word(Direction.Down, startP, endP)
                    startP = Position(i + 1, j)
                else:
                    endP = Position(i, j)
                    newWord = Word(Direction.Down, startP, endP)
            if newWord.length > 1:
                newWord = Word(Direction.Down, startP, endP)
                self.words_list.append(newWord)

        print("Variables are: " + str(len(self.words_list)))

        self.fill_crosswords()
        return self.words_list

    def fill_crosswords(self):
        for var1 in self.words_list:
            for var2 in self.words_list:
                if var1 != var2:
                    if self.is_crosswords(var1, var2):
                        if var1.direction == Direction.Across:
                            int_at = Position(var1.start.i, var2.start.j)
                            var1.add_crossword(int_at, var2)
                        else:
                            int_at = Position(var2.start.i, var1.start.j)
                            var1.add_crossword(int_at, var2)

    def is_crosswords(self, var1, var2):
        if var1.direction == Direction.Across:
            if var1.start.i >= var2.start.i and var1.start.i <= var2.end.i and var2.end.j <= var1.end.j and var2.end.j >= var1.start.j:
                return True
        else:
            if var2.start.i >= var1.start.i and var2.start.i <= var1.end.i and var1.end.j <= var2.end.j and var1.end.j >= var2.start.j:
                return True
        return False

    def print_grid(self, grid):
        grid_letters = [" "]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                grid_letters += str(val)
            grid_letters += ["\n"]

        result = " ".join(grid_letters)
        print(result[1:])
        print("--------------")

    def get_full_grid_by_list_of_words(self, list):
        grid = copy.deepcopy(self.grid)
        for word in list:
            if word.direction == Direction.Across:
                i = word.start.i
                k = word.start.j
                for j in range(word.start.j, word.end.j + 1):
                    if len(word.value) != 0:
                        if grid[i][j] == 1:
                            grid[i][j] = word.value[j - k]
                    else:
                        grid[i][j] = '1'
            else:
                j = word.start.j
                k = word.start.i
                for i in range(word.start.i, word.end.i + 1):
                    if len(word.value) != 0:
                        if grid[i][j] == 1:
                            grid[i][j] = word.value[i - k]
                    else:
                        grid[i][j] = '1'

        return grid
