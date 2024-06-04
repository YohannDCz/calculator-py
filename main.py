from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.resize(250, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.lineEdit = QLineEdit()  # Create QLineEdit
        layout.addWidget(self.lineEdit)  # Add QLineEdit to layout

        grid = QGridLayout()
        buttons = ["C", "+/-", "%", "/",
                   "7", "8", "9", "*",
                   "4", "5", "6", "-",
                   "1", "2", "3", "+",
                   ]

        for i, text in enumerate(buttons):
            row = i // 4
            col = i % 4
            button = QPushButton(text)
            grid.addWidget(button, row, col)
            button.clicked.connect(self.on_button_click)
        layout.addLayout(grid)

        row = QHBoxLayout()
        button1 = QPushButton("0")
        button2 = QPushButton(".")
        button3 = QPushButton("=")
        row.addWidget(button1, 2)
        row.addWidget(button2, 1)
        row.addWidget(button3, 1)
        button1.clicked.connect(self.on_button_click)
        button2.clicked.connect(self.on_button_click)
        button3.clicked.connect(self.on_button_click)
        layout.addLayout(row)

    def on_button_click(self):
        print("Button clicked")
        button = app.sender()
        text = button.text()

        if text == "=":
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        elif text == "C":
            self.lineEdit.clear()
        elif text == "+/-":
            self.lineEdit.setText(str(-1 * float(self.lineEdit.text())))
        else: # Add text to QLineEdit
            self.lineEdit.setText(self.lineEdit.text() + text)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    