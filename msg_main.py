# Form implementation - Fixed version
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from inquiry import Ui_InquiryWindow

# Simple Inquiry Window class (since we don't have the inquiry.py file)

   



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 914)
        MainWindow.setWindowTitle("Messaging Center")
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Chat info panel
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
        
        # Chat label
        self.label_2 = QtWidgets.QLabel(parent=self.chat_info)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setText("Chats")
        self.label_2.setObjectName("label_2")
        
        # Edit button
        self.push_edit = QtWidgets.QPushButton(parent=self.chat_info)
        self.push_edit.setGeometry(QtCore.QRect(150, 20, 75, 24))
        self.push_edit.setStyleSheet("""
            QPushButton#push_edit {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                padding: 4px;
            }
            QPushButton#push_edit:hover {
                background-color: #005a2e;
                color: white;
            }
            QPushButton#push_edit:pressed {
                background-color: #002d17;
            }
        """)
        self.push_edit.setText("Edit")
        self.push_edit.setObjectName("push_edit")
        
        # Search bar
        self.search_recipt = QtWidgets.QLineEdit(parent=self.chat_info)
        self.search_recipt.setGeometry(QtCore.QRect(10, 60, 211, 31))
        self.search_recipt.setStyleSheet("""
            QLineEdit {
                background-color: #f5f5f5;
                border: 1px solid #cfcfcf;
                border-radius: 15px;
                padding: 6px 12px;
                font-size: 13px;
            }
        """)
        self.search_recipt.setPlaceholderText("Search conversations...")
        self.search_recipt.setObjectName("search_recipt")
        
        # Horizontal line
        self.line = QtWidgets.QFrame(parent=self.chat_info)
        self.line.setGeometry(QtCore.QRect(0, 90, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        
        # Filter buttons layout
        self.layoutWidget = QtWidgets.QWidget(parent=self.chat_info)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 201, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
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
        
        # Filter buttons
        self.push_unread = QtWidgets.QPushButton("Unread")
        self.push_unread.setStyleSheet(button_style)
        self.push_unread.setObjectName("push_unread")
        self.horizontalLayout.addWidget(self.push_unread)
        
        self.push_all = QtWidgets.QPushButton("All")
        self.push_all.setStyleSheet(button_style)
        self.push_all.setObjectName("push_all")
        self.horizontalLayout.addWidget(self.push_all)
        
        self.push_comm = QtWidgets.QPushButton("Comm")
        self.push_comm.setStyleSheet(button_style)
        self.push_comm.setObjectName("push_comm")
        self.horizontalLayout.addWidget(self.push_comm)
        
        self.push_group = QtWidgets.QPushButton("Group")
        self.push_group.setStyleSheet(button_style)
        self.push_group.setObjectName("push_group")
        self.horizontalLayout.addWidget(self.push_group)
        
        # Chat list area (placeholder for now)
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
        
        # Add some sample chat items
        for i in range(5):
            item = QtWidgets.QListWidgetItem(f"Chat {i+1}")
            self.chat_list.addItem(item)
        
        # Main message area
        self.message_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.message_widget.setGeometry(QtCore.QRect(250, 100, 621, 771))
        self.message_widget.setStyleSheet("""
            QWidget#message_widget {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)
        self.message_widget.setObjectName("message_widget")
        
        # "No message found" label
        self.label_8 = QtWidgets.QLabel(parent=self.message_widget)
        self.label_8.setGeometry(QtCore.QRect(200, 310, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setText("No message found!")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        
        # Create Inquiry button
        self.create_inquiry = QtWidgets.QPushButton(parent=self.message_widget)
        self.create_inquiry.setGeometry(QtCore.QRect(200, 370, 231, 51))
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
        self.create_inquiry.setText("Create an Inquiry")
        self.create_inquiry.setObjectName("create_inquiry")
        
        # Contact info panel
        self.contact_info = QtWidgets.QWidget(parent=self.centralwidget)
        self.contact_info.setGeometry(QtCore.QRect(880, 100, 221, 771))
        self.contact_info.setStyleSheet("""
            QWidget#contact_info {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)
        self.contact_info.setObjectName("contact_info")
        
        # Contact info label
        self.label_9 = QtWidgets.QLabel(parent=self.contact_info)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setText("Contact Info")
        self.label_9.setObjectName("label_9")
        
        # Contact info separator line
        self.line_2 = QtWidgets.QFrame(parent=self.contact_info)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 221, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        
        # Contact details placeholder
        self.contact_details = QtWidgets.QLabel(parent=self.contact_info)
        self.contact_details.setGeometry(QtCore.QRect(10, 80, 201, 200))
        self.contact_details.setText("Select a conversation\nto view contact details")
        self.contact_details.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.contact_details.setWordWrap(True)
        self.contact_details.setStyleSheet("color: #666; font-size: 14px;")
        
        # Header label
        self.msg_header = QtWidgets.QLabel(parent=self.centralwidget)
        self.msg_header.setGeometry(QtCore.QRect(20, 40, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        self.msg_header.setFont(font)
        self.msg_header.setStyleSheet("""
            QLabel#msg_header {
                color: #084924;
                font-size: 25px;
                font-weight: bold;
                background-color: transparent;
            }
        """)
        self.msg_header.setText("Messaging Center")
        self.msg_header.setObjectName("msg_header")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu bar
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Store reference to inquiry window
        self.inquiry_window = None
        
        # Connect the "Create Inquiry" button
        self.ui.create_inquiry.clicked.connect(self.open_inquiry_window)
        
        # Connect filter buttons (add functionality as needed)
        self.ui.push_all.clicked.connect(lambda: self.filter_chats("all"))
        self.ui.push_unread.clicked.connect(lambda: self.filter_chats("unread"))
        self.ui.push_comm.clicked.connect(lambda: self.filter_chats("comm"))
        self.ui.push_group.clicked.connect(lambda: self.filter_chats("group"))
        
        # Connect search functionality
        self.ui.search_recipt.textChanged.connect(self.search_chats)
        
        # Connect chat list selection
        self.ui.chat_list.itemClicked.connect(self.on_chat_selected)

    def open_inquiry_window(self):
        """Open the inquiry window"""
        try:
            if self.inquiry_window is None or not self.inquiry_window.isVisible():
                self.inquiry_window = QtWidgets.QMainWindow()
                self.inquiry_ui = Ui_InquiryWindow()
                self.inquiry_ui.setupUi(self.inquiry_window)
                self.inquiry_window.show()
            else:
                # Bring existing window to front
                self.inquiry_window.raise_()
                self.inquiry_window.activateWindow()
        except Exception as e:
            print(f"Error opening inquiry window: {e}")
    
    def filter_chats(self, filter_type):
        """Filter chats based on type"""
        print(f"Filtering chats by: {filter_type}")
        # Add your filtering logic here
        
    def search_chats(self, text):
        """Search through chats"""
        print(f"Searching for: {text}")
        # Add your search logic here
        
    def on_chat_selected(self, item):
        """Handle chat selection"""
        chat_name = item.text()
        print(f"Selected chat: {chat_name}")
        # Update the message area and contact info
        self.ui.label_8.setText(f"Chat with {chat_name}")
        self.ui.contact_details.setText(f"Contact: {chat_name}\nStatus: Online\nLast seen: Now")

# Entry point
if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        
        # Set application style
        app.setStyle('Fusion')
        
        window = MainApp()
        window.show()
        
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"Application error: {e}")
        sys.exit(1)