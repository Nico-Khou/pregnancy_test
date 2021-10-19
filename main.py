import sys
from model import Model
from PySide6 import QtCore, QtWidgets, QtGui
from qt_material import apply_stylesheet


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        self.model = Model()
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)
        self.group = QtWidgets.QGroupBox('Test de grossesse')
        self.layout.addWidget(self.group)

        self.text = QtWidgets.QLabel('', alignment=QtCore.Qt.AlignCenter)
        self.result_title = QtWidgets.QLabel('-', alignment=QtCore.Qt.AlignCenter)
        self.result = QtWidgets.QLabel('-', alignment=QtCore.Qt.AlignCenter)

        self.group_result = QtWidgets.QGroupBox('Prédictions')
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(self.result_title)
        self.h_layout.addWidget(self.result)
        self.group_result.setLayout(self.h_layout)

        self.button = QtWidgets.QPushButton('Importer une image')

        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.addWidget(self.text)
        self.v_layout.addStretch()
        self.v_layout.addWidget(self.group_result)
        self.v_layout.addWidget(self.button)
        self.group.setLayout(self.v_layout)

        self.button.clicked.connect(self.get_file)

    @QtCore.Slot()
    def get_file(self):
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './test', 'Image files (*.jpg)')
        if file_name:
            self.text.setPixmap(QtGui.QPixmap(file_name))
            result, accuracy = self.model.evaluate(file_name)
            self.result_title.setText(result)
            self.result.setText(accuracy)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')

    widget = MyWidget()
    widget.setWindowTitle('Test de grossesse')
    widget.resize(480, 600)
    widget.show()

    sys.exit(app.exec())
