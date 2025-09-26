import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from inquiry import InquiryDialog
from recipient_dialog import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 914)
        MainWindow.setWindowTitle("Messaging Center")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

        # ===== Chat Info Panel =====
        self.chat_info = QtWidgets.QWidget(parent=self.centralwidget)
        self.chat_info.setGeometry(QtCore.QRect(10, 100, 231, 771))
        self.chat_info.setStyleSheet("""
            QWidget#chat_info {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)
        self.chat_info.setObjectName("chat_info")

        self.label_2 = QtWidgets.QLabel("Chats", parent=self.chat_info)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 61))
        font = QtGui.QFont("Arial", 18)
        self.label_2.setFont(font)

        self.push_edit = QtWidgets.QPushButton("Edit", parent=self.chat_info)
        self.push_edit.setGeometry(QtCore.QRect(150, 20, 75, 24))
        self.push_edit.setStyleSheet("""
            QPushButton {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #005a2e;
                color: white;
            }
            QPushButton:pressed {
                background-color: #002d17;
            }
        """)

        self.search_recipt = QtWidgets.QLineEdit(parent=self.chat_info)
        self.search_recipt.setGeometry(QtCore.QRect(10, 60, 211, 31))
        self.search_recipt.setPlaceholderText("Search conversations...")
        self.search_recipt.setStyleSheet("""
            QLineEdit {
                background-color: #f5f5f5;
                border: 1px solid #cfcfcf;
                border-radius: 15px;
                padding: 6px 12px;
                font-size: 13px;
            }
        """)

        self.line = QtWidgets.QFrame(parent=self.chat_info)
        self.line.setGeometry(QtCore.QRect(0, 90, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        # Filter buttons
        self.layoutWidget = QtWidgets.QWidget(parent=self.chat_info)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 201, 30))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        button_style = """
            QPushButton {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 12px;
                padding: 4px 8px;
                min-width: 40px;
            }
            QPushButton:hover {
                background-color: #005a2e;
                color: white;
            }
            QPushButton:pressed {
                background-color: #002d17;
            }
        """
        self.push_unread = QtWidgets.QPushButton("Unread")
        self.push_unread.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.push_unread)

        self.push_all = QtWidgets.QPushButton("All")
        self.push_all.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.push_all)

        self.push_comm = QtWidgets.QPushButton("Comm")
        self.push_comm.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.push_comm)

        self.push_group = QtWidgets.QPushButton("Group")
        self.push_group.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.push_group)

        # Chat list
        self.chat_list = QtWidgets.QListWidget(parent=self.chat_info)
        self.chat_list.setGeometry(QtCore.QRect(10, 150, 201, 450))
        self.chat_list.setStyleSheet("""
            QListWidget {
                border: none;
                background-color: transparent;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
        """)
        for i in range(5):
            self.chat_list.addItem(QtWidgets.QListWidgetItem(f"Chat {i+1}"))

        # ===== Message Widget =====
        self.message_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.message_widget.setGeometry(QtCore.QRect(250, 100, 621, 771))
        self.message_widget.setObjectName("message_widget")
        self.message_widget.setStyleSheet("""
            QWidget#message_widget {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)

        self.label_8 = QtWidgets.QLabel("No message found!", parent=self.message_widget)
        self.label_8.setGeometry(QtCore.QRect(200, 310, 241, 61))
        self.label_8.setFont(QtGui.QFont("Arial", 20))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.create_inquiry = QtWidgets.QPushButton("Create an Inquiry", parent=self.message_widget)
        self.create_inquiry.setGeometry(QtCore.QRect(200, 370, 231, 51))
        self.create_inquiry.setObjectName("create_inquiry")
        self.create_inquiry.setStyleSheet("""
            QPushButton#create_inquiry {
                background-color: #003d1f;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 10px;
                padding: 8px 20px;
                font-size: 14px;
            }
            QPushButton#create_inquiry:hover {
                background-color: #005a2e;
            }
            QPushButton#create_inquiry:pressed {
                background-color: #002d17;
            }
        """)

        # ===== Contact Info Panel =====
        self.contact_info = QtWidgets.QWidget(parent=self.centralwidget)
        self.contact_info.setGeometry(QtCore.QRect(880, 100, 221, 771))
        self.contact_info.setObjectName("contact_info")
        self.contact_info.setStyleSheet("""
            QWidget#contact_info {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)

        self.label_9 = QtWidgets.QLabel("Contact Info", parent=self.contact_info)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 181, 61))
        self.label_9.setFont(QtGui.QFont("Arial", 18))

        self.line_2 = QtWidgets.QFrame(parent=self.contact_info)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 221, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)

        self.contact_details = QtWidgets.QLabel(
            "Select a conversation\nto view contact details",
            parent=self.contact_info
        )
        self.contact_details.setGeometry(QtCore.QRect(10, 80, 201, 200))
        self.contact_details.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.contact_details.setWordWrap(True)
        self.contact_details.setStyleSheet("color: #666; font-size: 14px;")

        # ===== Header =====
        self.msg_header = QtWidgets.QLabel("Messaging Center", parent=self.centralwidget)
        self.msg_header.setGeometry(QtCore.QRect(20, 40, 221, 61))
        self.msg_header.setStyleSheet("""
            QLabel#msg_header {
                color: #084924;
                font-size: 25px;
                font-weight: bold;
                background-color: transparent;
            }
        """)
        self.msg_header.setObjectName("msg_header")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(QtWidgets.QMenuBar(parent=MainWindow))
        MainWindow.setStatusBar(QtWidgets.QStatusBar(parent=MainWindow))


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.create_inquiry.clicked.connect(self.open_inquiry_dialog)
        self.ui.push_all.clicked.connect(lambda: self.filter_chats("all"))
        self.ui.push_unread.clicked.connect(lambda: self.filter_chats("unread"))
        self.ui.push_comm.clicked.connect(lambda: self.filter_chats("comm"))
        self.ui.push_group.clicked.connect(lambda: self.filter_chats("group"))
        self.ui.search_recipt.textChanged.connect(self.search_chats)
        self.ui.chat_list.itemClicked.connect(self.on_chat_selected)
        

    def open_inquiry_dialog(self):
        dialog = InquiryDialog(self)
        if dialog.exec():
            print("Inquiry Created!")
        else:
            print("Inquiry Cancelled")

    def filter_chats(self, filter_type):
        print(f"Filtering chats by: {filter_type}")

    def search_chats(self, text):
        print(f"Searching for: {text}")

    def on_chat_selected(self, item):
        chat_name = item.text()
        self.ui.label_8.setText(f"Chat with {chat_name}")
        self.ui.contact_details.setText(f"Contact: {chat_name}\nStatus: Online\nLast seen: Now")
    
    def open_recipient_dialog(self):
        """Function to open the recipient selection dialog"""
        dialog = Ui_Form(self)
        if dialog.exec():
            print("Recipient Selected!")
        else:
            print("Recipient Selection Cancelled")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainApp()
    window.show()
    sys.exit(app.exec())
