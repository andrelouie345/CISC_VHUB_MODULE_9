import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from inquiry import InquiryDialog
from recipient_dialog import Ui_Form
from sidebar import Sidebar
from header import Header

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 914)
        MainWindow.setWindowTitle("Messaging Center")
        MainWindow.setMinimumSize(1980, 1080)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        
        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===== Header =====
        self.header = Header(parent=self.centralwidget)
        self.header.setFixedHeight(84)
        main_layout.addWidget(self.header)

        # Content area
        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 16, 0, 16)
        content_layout.setSpacing(16)

        # ===== Sidebar placeholder (will be added dynamically) =====
        self.sidebar_container = QtWidgets.QWidget()
        self.sidebar_container.setFixedWidth(250)
        content_layout.addWidget(self.sidebar_container)

        # ===== Chat Info Panel =====
        self.chat_info = QtWidgets.QWidget()
        self.chat_info.setMinimumWidth(231)
        self.chat_info.setMaximumWidth(280)
        self.chat_info.setStyleSheet("""
            QWidget#chat_info {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
            }
        """)
        self.chat_info.setObjectName("chat_info")

        chat_layout = QtWidgets.QVBoxLayout(self.chat_info)
        chat_layout.setContentsMargins(10, 10, 10, 10)
        chat_layout.setSpacing(10)

        # Chat header
        chat_header_layout = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel("Chats")
        self.label_2.setFont(QtGui.QFont("Arial", 18))
        chat_header_layout.addWidget(self.label_2)
        chat_header_layout.addStretch()

        self.push_edit = QtWidgets.QPushButton("Edit")
        self.push_edit.setStyleSheet("""
            QPushButton {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                padding: 4px 8px;
            }
            QPushButton:hover {
                background-color: #005a2e;
                color: white;
            }
            QPushButton:pressed {
                background-color: #002d17;
            }
        """)
        chat_header_layout.addWidget(self.push_edit)
        chat_layout.addLayout(chat_header_layout)

        # Search box
        self.search_recipt = QtWidgets.QLineEdit()
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
        chat_layout.addWidget(self.search_recipt)

        # Separator
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        chat_layout.addWidget(self.line)

        # Filter buttons
        filter_layout = QtWidgets.QHBoxLayout()
        button_style = """
            QPushButton {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 12px;
                padding: 4px 8px;
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
        filter_layout.addWidget(self.push_unread)

        self.push_all = QtWidgets.QPushButton("All")
        self.push_all.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_all)

        self.push_comm = QtWidgets.QPushButton("Comm")
        self.push_comm.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_comm)

        self.push_group = QtWidgets.QPushButton("Group")
        self.push_group.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_group)

        chat_layout.addLayout(filter_layout)

        # Chat list
        self.chat_list = QtWidgets.QListWidget()
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
        chat_layout.addWidget(self.chat_list)

        content_layout.addWidget(self.chat_info)

        # ===== Message Widget =====
        self.message_widget = QtWidgets.QWidget()
        self.message_widget.setObjectName("message_widget")
        self.message_widget.setStyleSheet("""
            QWidget#message_widget {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
            }
        """)

        message_layout = QtWidgets.QVBoxLayout(self.message_widget)
        message_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.label_8 = QtWidgets.QLabel("No message found!")
        self.label_8.setFont(QtGui.QFont("Arial", 20))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        message_layout.addWidget(self.label_8)

        self.create_inquiry = QtWidgets.QPushButton("Create an Inquiry")
        self.create_inquiry.setObjectName("create_inquiry")
        self.create_inquiry.setFixedSize(231, 51)
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
        message_layout.addWidget(self.create_inquiry, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        content_layout.addWidget(self.message_widget, stretch=1)

        # ===== Contact Info Panel =====
        self.contact_info = QtWidgets.QWidget()
        self.contact_info.setMinimumWidth(221)
        self.contact_info.setMaximumWidth(280)
        self.contact_info.setObjectName("contact_info")
        self.contact_info.setStyleSheet("""
            QWidget#contact_info {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
            }
        """)

        contact_layout = QtWidgets.QVBoxLayout(self.contact_info)
        contact_layout.setContentsMargins(10, 10, 10, 10)
        contact_layout.setSpacing(10)

        self.label_9 = QtWidgets.QLabel("Contact Info")
        self.label_9.setFont(QtGui.QFont("Arial", 18))
        contact_layout.addWidget(self.label_9)

        self.line_2 = QtWidgets.QFrame()
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        contact_layout.addWidget(self.line_2)

        self.contact_details = QtWidgets.QLabel(
            "Select a conversation\nto view contact details"
        )
        self.contact_details.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.contact_details.setWordWrap(True)
        self.contact_details.setStyleSheet("color: #666; font-size: 14px;")
        contact_layout.addWidget(self.contact_details)
        contact_layout.addStretch()

        content_layout.addWidget(self.contact_info)

        main_layout.addWidget(content_widget)
        MainWindow.setCentralWidget(self.centralwidget)

    def add_sidebar(self, sidebar_widget):
        # Clear any existing widget in sidebar container
        layout = self.sidebar_container.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.sidebar_container)
            layout.setContentsMargins(0, 0, 0, 0)
        
        sidebar_widget.setParent(self.sidebar_container)
        layout.addWidget(sidebar_widget)
    
    def update_sidebar_width(self, is_collapsed):
        """Update sidebar container width based on collapse state"""
        if is_collapsed:
            self.sidebar_container.setFixedWidth(60)  # Collapsed width
        else:
            self.sidebar_container.setFixedWidth(250)  # Expanded width


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create and add sidebar
        self.sidebar = Sidebar()
        self.ui.add_sidebar(self.sidebar)

        # Connect sidebar toggle button to update container width
        self.sidebar.toggle_btn.clicked.connect(self.on_sidebar_toggle)

        # Connect header actions
        self.connect_header_actions()

        # Connect buttons
        self.ui.create_inquiry.clicked.connect(self.open_inquiry_dialog)
        self.ui.push_all.clicked.connect(lambda: self.filter_chats("all"))
        self.ui.push_unread.clicked.connect(lambda: self.filter_chats("unread"))
        self.ui.push_comm.clicked.connect(lambda: self.filter_chats("comm"))
        self.ui.push_group.clicked.connect(lambda: self.filter_chats("group"))
        self.ui.search_recipt.textChanged.connect(self.search_chats)
        self.ui.chat_list.itemClicked.connect(self.on_chat_selected)

    def connect_header_actions(self):
        """Connect header menu actions to methods"""
        actions = self.ui.header.profile_menu.actions()
        for action in actions:
            if action.text() == "My Profile":
                action.triggered.connect(self.show_profile)
            elif action.text() == "Log Out":
                action.triggered.connect(self.logout)

    def show_profile(self):
        """Show user profile"""
        print("Opening profile...")
        QtWidgets.QMessageBox.information(self, "Profile", "Profile feature coming soon!")

    def logout(self):
        """Handle logout"""
        reply = QtWidgets.QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to logout?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Logging out...")
            self.close()

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
    
    def update_sidebar_container(self):
        """Update the sidebar container width based on sidebar's current state"""
        self.ui.update_sidebar_width(self.sidebar.is_collapsed)
    
    def on_sidebar_toggle(self):
        """Handle sidebar toggle - check if sidebar is collapsed"""
        # The sidebar's is_collapsed state gets updated in toggleDrawer
        # We need to check it after the toggle happens
        # Use QTimer to check state after the toggle completes
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(50, self.update_sidebar_container)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainApp()
    window.show()
    sys.exit(app.exec())