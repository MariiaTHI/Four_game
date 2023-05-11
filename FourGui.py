import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt

from CircleWidget import CircleWidget
from Four import Four


class FourGui(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.game_layout = QtWidgets.QVBoxLayout()
        self.game_layout.setSpacing(0)
        self.game_layout.setMargin(0)

        header_layout = QtWidgets.QHBoxLayout()

        self.text = QtWidgets.QLabel("Player")
        self.text.setFixedHeight(20)
        header_layout.addWidget(self.text)

        button = QtWidgets.QPushButton("Restart Game")
        button.setFixedWidth(200)
        button.clicked.connect(self.restart_game)
        header_layout.addWidget(button)

        self.game_layout.addLayout(header_layout)
        self.setLayout(self.game_layout)

        self.game = Four()
        self.won = False

        self.update_player_text()

        self.grid_css = "border: 1px solid black;"
        self.init_game_grid()

    def update_player_text(self):
        if self.won:
            self.text.setText(f"{self.game.active_player} player won the game!" )
            self.text.setStyleSheet(f"background-color: green; padding-left: 10px")
        else:
            self.text.setText(self.game.active_player)
            self.text.setStyleSheet(f"background-color: {self.game.active_player}; padding-left: 10px")

    def restart_game(self):
        self.game = Four()
        self.won = False
        self.update_game_grid()
        self.update_player_text()

    def init_game_grid(self):
        layout = QtWidgets.QGridLayout()
        layout.setSpacing(0)
        layout.setMargin(0)
        for r in range(self.game.rows):
            for c in range(self.game.columns):
                spacer = QtWidgets.QWidget()
                spacer.setStyleSheet(self.grid_css)
                layout.addWidget(spacer, r, c)

        self.game_layout.addLayout(layout)

    def update_game_grid(self):
        layout = None
        for i, l in enumerate(self.layout().children()):
            if isinstance(l, QtWidgets.QGridLayout):
                layout = l

        if not layout:
            raise Exception("grid layout not found")

        for r in range(self.game.rows):
            for c in range(self.game.columns):
                if self.game.field[r][c] == "_":
                    spacer = QtWidgets.QWidget()
                    spacer.setStyleSheet(self.grid_css)
                    layout.itemAtPosition(r, c).wid.deleteLater()
                    layout.addWidget(spacer, r, c)
                else:
                    if self.game.field[r][c] == "R":
                        circle = CircleWidget(Qt.red)
                    else:
                        circle = CircleWidget(Qt.yellow)
                    circle.setStyleSheet(self.grid_css)
                    layout.itemAtPosition(r, c).wid.deleteLater()
                    layout.addWidget(circle, r, c)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if not self.won:
            if event.y() < 20:
                return
            column = event.x() // 100
            print((event.x()))
            column = column if column <= self.game.columns else self.game.columns
            self.won = self.game.run_one_round(column)
            self.update_game_grid()
            self.update_player_text()
            self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = FourGui()
    widget.resize(700, 620)
    widget.show()

    sys.exit(app.exec_())
