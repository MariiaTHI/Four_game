class Four:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.field = [["_", "_", "_", "_", "_", "_", "_"],
                 ["_", "_", "_", "_", "_", "_", "_"],
                 ["_", "_", "_", "_", "_", "_", "_"],
                 ["_", "_", "_", "_", "_", "_", "_"],
                 ["_", "_", "_", "_", "_", "_", "_"],
                 ["_", "_", "_", "_", "_", "_", "_"]]
        self.active_player = "Red"
        self.running = True

    def set_coin(self, col_nr):
        if self.active_player == 'Red':
            player = 'R'
        else:
            player = 'Y'

        if self.field[0][col_nr] == 'R' or self.field[0][col_nr] == 'Y':
            print(f"The column {col_nr} is already full.....Try another column !")
            return False

        else:
            for i in range(6):

                if self.field[i][col_nr] == "R" or self.field[i][col_nr] == "Y":
                    self.field[i - 1][col_nr] = player
                    break

                if i == 5:
                    self.field[i][col_nr] = player

            return True

    def show_field(self):
        for line in self.field:
            print(*line)

    def winner_check(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.field[i][j] != '_':
                    # check for horizontal
                    if j + 3 < self.columns and self.field[i][j] == self.field[i][j + 1] and self.field[i][j] == self.field[i][j + 2] and \
                            self.field[i][j] == self.field[i][j + 3]:
                        print(f"{self.field[i][j]} won")
                        return True  # ADDED

                    # check vertical
                    if self.field[i][j] != '_':
                        if i + 3 < self.rows and self.field[i][j] == self.field[i + 1][j] == self.field[i + 2][j] == \
                                self.field[i + 3][j]:
                            return True

                    # Ueberpruefe, ob es eine Reihe nach rechts unten gibt
                    if i + 3 < self.rows and j + 3 < self.columns and self.field[i][j] == self.field[i + 1][j + 1] == \
                            self.field[i + 2][j + 2] == self.field[i + 3][j + 3]:
                        return [(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)]
                    # Ueberpruefe, ob es eine Reihe nach links unten gibt
                    if i - 3 < self.rows and j + 3 < self.columns and self.field[i][j] == self.field[i - 1][j + 1] == \
                            self.field[i - 2][j + 2] == self.field[i - 3][j + 3]:
                        return [(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)]

    def run(self):
        while self.running:
            # game is happening
            col_nr = int(input("chose a rows"))
            if self.run_one_round(col_nr):
                break

    def run_one_round(self, col_nr):
        self.set_coin(col_nr)
        self.show_field()

        if self.winner_check():  # ADDED
            print("the winner is " + self.active_player)
            self.running = False
            return True

        if self.active_player == "Red":
            self.active_player = "Yellow"
        else:
            self.active_player = "Red"
        return False


if __name__ == "__main__":
    game = Four()
    game.run()
