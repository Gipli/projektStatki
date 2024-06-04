class boardTwoPlayers:
    def __init__(self):
        rows, cols = (10, 10)
        self.board1 = [[0 for i in range(cols)] for j in range(rows)]
        self.board2 = [[0 for i in range(cols)] for j in range(rows)]
        self.orientation1 = [0, 0, 0, 0, 0]
        self.orientation2 = [0, 0, 0, 0, 0]
        self.ships = [5,4,3,3,2]
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.cords1 = [[0 for i in range(17)] for j in range(2)]
        self.cords2 = [[0 for i in range(17)] for j in range(2)]
        self.cord1Counter = 0
        self.cord2Counter = 0

    def orient1(self):
        print("P1: W jakiej orientacji chcesz miec swoje statki (poz/pion):")
        for i in range(5):
            choice = input(f'{i + 1}: ')
            if choice == "pion":
                self.orientation1[i] = 1

    def orient2(self):
        print("P2: W jakiej orientacji chcesz miec swoje statki (poz/pion):")
        for i in range(5):
            choice = input(f'{i + 1}: ')
            if choice == "pion":
                self.orientation1[i] = 1

    def printBoard1(self):
        print("   ", end="")
        for letter in self.letters:
            print(letter, end="  ")
        print()
        for i in range(10):
            print(f'{i}: {self.board1[i]}')

    def printBoard2(self):
        print("   ", end="")
        for letter in self.letters:
            print(letter, end="  ")
        print()
        for i in range(10):
            print(f'{i}: {self.board2[i]}')

    def inputIncorrect(self,x, y, i, isLetter, wrongAttempts, p):
        if wrongAttempts == 0:
            return True
        if isLetter == False:
            print("Koordynaty poza plansza")
            return True
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Koordynaty poza plansza")
            return True
        if self.orientation1[i] == 0:
            if y + self.ships[i] > 9:
                print("Statek poza plansza")
                return True
            for j in range(self.ships[i]):
                if p == 1:
                    if self.board1[x][y + j]:
                        print("Kolizja")
                        return True
                if p == 2:
                    if self.board2[x][y + j]:
                        print("Kolizja")
                        return True
        if self.orientation1[i] == 1:
            if x + self.ships[i] > 9:
                print("Statek poza plansza")
                return True
            for j in range(self.ships[i]):
                if p == 1:
                    if self.board1[x + j][y]:
                        print("Kolizja")
                        return True

                if p == 2:
                    if self.board2[x + j][y]:
                        print("Kolizja")
                        return True
        return False
#Vektoryzowac istniejace koordynaty statkow aby sprawdzac czy sie nie stykaja
    def askP1(self):
        self.printBoard1()
        for i in range(5):
            x = -1
            y = -1
            isLetter = True
            wrongAttempts = 0
            while self.inputIncorrect(x, y, i, isLetter, wrongAttempts, 1):
                y = str(input(f'P1: Podaj koordynaty poziomu poczatku statku o rozmiarze {self.ships[i]}: '))
                x = int(input(f'P1: Podaj koordynaty pionu poczatku statku o rozmiarze {self.ships[i]}: '))
                isLetter = False
                for j in range(10):
                    if y == self.letters[j]:
                        isLetter = True
                        y = int(j)
                wrongAttempts += 1
            if self.orientation1[i] == 0:
                for j in range(self.ships[i]):
                    self.board1[x][y] = 1
                    self.cords1[self.cord1Counter][0] = x
                    self.cords1[self.cord1Counter][1] = y
                    self.cord1Counter += 1
                    y += 1
            else:
                for j in range(self.ships[i]):
                    self.board1[x][y] = 1
                    self.cords1[self.cord1Counter][0] = x
                    self.cords1[self.cord1Counter][1] = y
                    self.cord1Counter += 1
                    x += 1
            self.printBoard1()

    def askP2(self):
        self.printBoard2()
        for i in range(5):
            x = -1
            y = -1
            isLetter = True
            wrongAttempts = 0
            while self.inputIncorrect(x, y, i, isLetter, wrongAttempts, 2):
                y = str(input(f'P2: Podaj koordynaty poziomu poczatku statku o rozmiarze {self.ships[i]}: '))
                x = int(input(f'P2: Podaj koordynaty pionu poczatku statku o rozmiarze {self.ships[i]}: '))
                isLetter = False
                for j in range(10):
                    if y == self.letters[j]:
                        isLetter = True
                        y = int(j)
                wrongAttempts += 1
            if self.orientation2[i] == 0:
                for j in range(self.ships[i]):
                    self.board2[x][y] = 1
                    y += 1
                    self.cords2[self.cord2Counter][0] = x
                    self.cords2[self.cord2Counter][1] = y
                    self.cord2Counter += 1
            else:
                for j in range(self.ships[i]):
                    self.board2[x][y] = 1
                    x += 1
                self.cords2[self.cord2Counter][0] = x
                self.cords2[self.cord2Counter][1] = y
                self.cord2Counter += 1
            self.printBoard2()
    def gameOver(self):
        if len(self.cords1) == 0 or len(self.cords2) == 0:
            return True
        return False
    #def guessCorrect(self, x, y):

    def game(self):
        turnCounter = 0
        while(self.gameOver() == False):
            if turnCounter % 2 == 0:
                missed = False
                hit = False
                while(missed == False):
                    #NOT INPUT SANITIZED
                    y = str(input(f'P1: Podaj koordynaty poziomu swojego strzalu: '))
                    x = int(input(f'P1: Podaj koordynaty pionu swojego strzalu: '))
                    for j in range(10):
                        if y == self.letters[j]:
                            y = int(j)
                    for i in range(len(self.cords2)):
                        if x == self.cords2[i][0] and y == self.cords2[i][1]:
                            print("Trafione!")
                            self.cords2.pop(i)
                            hit = True
                    if hit == True:
                        missed = False
                    if hit == False:
                        print("Pudło!")
                        missed = True
            if turnCounter % 2 != 0:
                missed = False
                hit = False
                while(missed == False):
                    #NOT INPUT SANITIZED
                    y = str(input(f'P2: Podaj koordynaty poziomu swojego strzalu: '))
                    x = int(input(f'P2: Podaj koordynaty pionu swojego strzalu: '))
                    for j in range(10):
                        if y == self.letters[j]:
                            y = int(j)
                    for i in range(len(self.cords1)):
                        if x == self.cords1[i][0] and y == self.cords1[i][1]:
                            print("Trafione!")
                            self.cords1.pop(i)
                            hit = True
                    if hit == True:
                        missed = False
                    if hit == False:
                        print("Pudło!")
                        missed = True
        if len(self.cords2) == 0:
            print("Zwyciezyl gracz nr 1!")

        if len(self.cords1) == 0:
            print("Zwyciezyl gracz nr 2!")



test = boardTwoPlayers()
test.orient1()
test.askP1()
test.orient2()
test.askP2()