from PyQt6 import QtWidgets
from main_chat import Ui_MainWindow

class MainChatWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, chat_name="Chat"):
        super().__init__(parent)

        # 🧩 Remove unwanted outer margins and spacing
        self.setContentsMargins(0, 0, 0, 0)

        # Create a dummy QMainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Embed its central widget inside this QWidget
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # ✅ Remove margins
        layout.setSpacing(0)                   # ✅ Remove spacing
        layout.addWidget(self.ui.centralwidget)

        self.ui.name_header.setText(chat_name)
