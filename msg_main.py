import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from inquiry import InquiryDialog
from recipient_dialog import Ui_Form
from sidebar import Sidebar
from header import Header
from data_manager import DataManager

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

        # Initialize data manager for handling all data operations
        self.data_manager = DataManager()
        
        # Set current user (you can change this to any user ID from dummy_data.json)
        self.current_user_id = 1  # Carlos Fidel Castro

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
        
        # Load real data from database
        self.load_chats_from_database()
        self.load_user_info()

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
            # Get the inquiry data from the dialog
            inquiry_data = dialog.get_inquiry_data()
            if inquiry_data:
                # Create inquiry using data manager
                created_inquiry = self.data_manager.create_inquiry(inquiry_data)
                if created_inquiry:
                    print(f"Inquiry Created! ID: {created_inquiry['id']}")
                    # Refresh the UI if needed
                    self.load_chats_from_database()
                else:
                    print("Failed to create inquiry")
            else:
                print("No inquiry data received")
        else:
            print("Inquiry Cancelled")

    def filter_chats(self, filter_type):
        """Filter conversations based on type (all, unread, comm, group)"""
        print(f"Filtering chats by: {filter_type}")
        
        # Clear current chat list
        self.ui.chat_list.clear()
        
        # Get conversations based on filter type
        user_conversations = []
        for conv in self.data_manager.data['conversations']:
            if self.current_user_id in conv.get('participants', []):
                if filter_type == "all":
                    user_conversations.append(conv)
                elif filter_type == "unread":
                    # Check if there are unread messages in this conversation
                    has_unread = False
                    for msg in self.data_manager.data['messages']:
                        if (msg.get('receiver_id') == self.current_user_id and 
                            not msg.get('is_read', False) and
                            ((msg.get('sender_id') in conv.get('participants', []) and 
                              msg.get('receiver_id') in conv.get('participants', [])))):
                            has_unread = True
                            break
                    if has_unread:
                        user_conversations.append(conv)
                elif filter_type == "comm" and conv.get('is_group', False):
                    user_conversations.append(conv)
                elif filter_type == "group" and conv.get('is_group', False):
                    user_conversations.append(conv)
        
        # Sort by last activity
        user_conversations.sort(key=lambda x: x.get('last_activity', ''), reverse=True)
        
        # Add filtered conversations to chat list
        for conv in user_conversations:
            if conv.get('is_group', False):
                chat_name = conv.get('group_name', f"Group {conv['id']}")
            else:
                other_participant_id = None
                for participant_id in conv.get('participants', []):
                    if participant_id != self.current_user_id:
                        other_participant_id = participant_id
                        break
                
                if other_participant_id:
                    other_user = self.data_manager.get_user(other_participant_id)
                    chat_name = other_user.get('name', f"User {other_participant_id}") if other_user else f"User {other_participant_id}"
                else:
                    chat_name = f"Chat {conv['id']}"
            
            self.ui.chat_list.addItem(chat_name)

    def search_chats(self, text):
        """Search conversations by participant names or group names"""
        print(f"Searching for: {text}")
        
        if not text.strip():
            # If search is empty, show all chats
            self.load_chats_from_database()
            return
        
        # Clear current chat list
        self.ui.chat_list.clear()
        
        # Search through conversations
        search_text = text.lower()
        matching_conversations = []
        
        for conv in self.data_manager.data['conversations']:
            if self.current_user_id in conv.get('participants', []):
                if conv.get('is_group', False):
                    # Group conversation
                    group_name = conv.get('group_name', '').lower()
                    if search_text in group_name:
                        matching_conversations.append(conv)
                else:
                    # Individual conversation - check other participant's name
                    other_participant_id = None
                    for participant_id in conv.get('participants', []):
                        if participant_id != self.current_user_id:
                            other_participant_id = participant_id
                            break
                    
                    if other_participant_id:
                        other_user = self.data_manager.get_user(other_participant_id)
                        if other_user and search_text in other_user.get('name', '').lower():
                            matching_conversations.append(conv)
        
        # Sort by last activity
        matching_conversations.sort(key=lambda x: x.get('last_activity', ''), reverse=True)
        
        # Add matching conversations to chat list
        for conv in matching_conversations:
            if conv.get('is_group', False):
                chat_name = conv.get('group_name', f"Group {conv['id']}")
            else:
                other_participant_id = None
                for participant_id in conv.get('participants', []):
                    if participant_id != self.current_user_id:
                        other_participant_id = participant_id
                        break
                
                if other_participant_id:
                    other_user = self.data_manager.get_user(other_participant_id)
                    chat_name = other_user.get('name', f"User {other_participant_id}") if other_user else f"User {other_participant_id}"
                else:
                    chat_name = f"Chat {conv['id']}"
            
            self.ui.chat_list.addItem(chat_name)

    def on_chat_selected(self, item):
        """Handle when a chat is selected from the list"""
        chat_name = item.text()
        
        # Find the conversation data
        conversation = self.get_conversation_by_chat_name(chat_name)
        
        if conversation:
            if conversation.get('is_group', False):
                # Group conversation
                self.ui.label_8.setText(f"Group: {chat_name}")
                self.ui.contact_details.setText(f"Group Chat\nParticipants: {len(conversation.get('participants', []))}\nLast Activity: {conversation.get('last_activity', 'Unknown')}")
            else:
                # Individual conversation
                other_participant_id = None
                for participant_id in conversation.get('participants', []):
                    if participant_id != self.current_user_id:
                        other_participant_id = participant_id
                        break
                
                if other_participant_id:
                    other_user = self.data_manager.get_user(other_participant_id)
                    if other_user:
                        status = other_user.get('status', 'offline')
                        last_seen = other_user.get('last_seen', 'Unknown')
                        department = other_user.get('department', 'Unknown')
                        role = other_user.get('role', 'Unknown')
                        
                        self.ui.label_8.setText(f"Chat with {other_user['name']}")
                        self.ui.contact_details.setText(f"Contact: {other_user['name']}\nRole: {role.title()}\nDepartment: {department}\nStatus: {status.title()}\nLast seen: {last_seen}")
                    else:
                        self.ui.label_8.setText(f"Chat with {chat_name}")
                        self.ui.contact_details.setText(f"Contact: {chat_name}\nStatus: Unknown")
                else:
                    self.ui.label_8.setText(f"Chat with {chat_name}")
                    self.ui.contact_details.setText(f"Contact: {chat_name}\nStatus: Unknown")
        else:
            # Fallback for unknown chat
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
    
    def load_chats_from_database(self):
        """Load real conversations from the database instead of placeholder data"""
        # Clear existing chat list
        self.ui.chat_list.clear()
        
        # Get all conversations involving the current user
        user_conversations = []
        for conv in self.data_manager.data['conversations']:
            if self.current_user_id in conv.get('participants', []):
                user_conversations.append(conv)
        
        # Sort conversations by last activity (most recent first)
        user_conversations.sort(key=lambda x: x.get('last_activity', ''), reverse=True)
        
        # Add conversations to the chat list
        for conv in user_conversations:
            if conv.get('is_group', False):
                # Group conversation
                chat_name = conv.get('group_name', f"Group {conv['id']}")
            else:
                # Individual conversation - find the other participant
                other_participant_id = None
                for participant_id in conv.get('participants', []):
                    if participant_id != self.current_user_id:
                        other_participant_id = participant_id
                        break
                
                if other_participant_id:
                    other_user = self.data_manager.get_user(other_participant_id)
                    chat_name = other_user.get('name', f"User {other_participant_id}") if other_user else f"User {other_participant_id}"
                else:
                    chat_name = f"Chat {conv['id']}"
            
            # Add to chat list
            self.ui.chat_list.addItem(chat_name)
    
    def load_user_info(self):
        """Load current user information and update header"""
        current_user = self.data_manager.get_user(self.current_user_id)
        if current_user:
            # Update header with current user info
            # You can modify the header.py to accept user data if needed
            print(f"Current user: {current_user['name']} ({current_user['role']})")
    
    def get_conversation_by_chat_name(self, chat_name):
        """Find conversation data by chat name"""
        for conv in self.data_manager.data['conversations']:
            if conv.get('is_group', False):
                if conv.get('group_name') == chat_name:
                    return conv
            else:
                # Individual conversation - find the other participant
                other_participant_id = None
                for participant_id in conv.get('participants', []):
                    if participant_id != self.current_user_id:
                        other_participant_id = participant_id
                        break
                
                if other_participant_id:
                    other_user = self.data_manager.get_user(other_participant_id)
                    if other_user and other_user.get('name') == chat_name:
                        return conv
        return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Load external QSS stylesheet
    try:
        with open("sidebar_styles.qss", "r") as f:
            app.setStyleSheet(f.read())
        print("✅ QSS stylesheet loaded successfully")
    except FileNotFoundError:
        print("⚠️  sidebar_styles.qss not found, using default styles")
        # Fallback: Set basic styles to prevent black background
        app.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
                color: #333333;
            }
            QWidget {
                background-color: #f8f9fa;
                color: #333333;
            }
        """)
    except Exception as e:
        print(f"❌ Error loading QSS: {e}")
        # Fallback: Set basic styles to prevent black background
        app.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
                color: #333333;
            }
            QWidget {
                background-color: #f8f9fa;
                color: #333333;
            }
        """)
    
    window = MainApp()
    window.show()
    sys.exit(app.exec())