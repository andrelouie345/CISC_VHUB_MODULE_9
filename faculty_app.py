"""
Faculty Application for CISC Virtual Hub Messaging System
========================================================

This is the main application for faculty members to manage their messages,
inquiries, and communications with students.

This app allows faculty to:
- View all messages and inquiries assigned to them
- Filter messages by priority, status, and type
- Respond to student inquiries
- Manage their message categories
"""

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from faculty.faculty_main import Ui_MainWindow
from data_manager import DataManager
from inquiry import InquiryDialog
from sidebar import Sidebar
from header import Header


class FacultyMainUI(QtWidgets.QWidget):
    """Custom UI class that includes sidebar and header for faculty app"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("FacultyMainUI")
        
        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===== Header =====
        self.header = Header(parent=self)
        self.header.setFixedHeight(84)
        main_layout.addWidget(self.header)

        # Content area
        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 8, 0, 8)
        content_layout.setSpacing(8)

        # ===== Sidebar placeholder (will be added dynamically) =====
        self.sidebar_container = QtWidgets.QWidget()
        self.sidebar_container.setFixedWidth(250)
        content_layout.addWidget(self.sidebar_container)

        # ===== Faculty Content Area =====
        self.faculty_content = QtWidgets.QWidget()
        self.faculty_content.setObjectName("faculty_content")
        
        # Create a custom faculty UI layout instead of using the generated one
        self.setup_faculty_content()
        
        content_layout.addWidget(self.faculty_content, stretch=1)
        main_layout.addWidget(content_widget)

    def setup_faculty_content(self):
        """Set up the faculty content area with proper layout"""
        # Main layout for faculty content
        faculty_layout = QtWidgets.QHBoxLayout(self.faculty_content)
        faculty_layout.setContentsMargins(0, 0, 0, 0)
        faculty_layout.setSpacing(8)

        # ===== Left Panel - Message Categories =====
        self.inquiry_widget = QtWidgets.QWidget()
        self.inquiry_widget.setMinimumWidth(251)
        self.inquiry_widget.setMaximumWidth(280)
        self.inquiry_widget.setStyleSheet("""
            QWidget#inquiry_widget {
                background-color: white;
                border-radius: 20px;
                border: 1px solid #dddddd;
            }
        """)
        self.inquiry_widget.setObjectName("inquiry_widget")

        inquiry_layout = QtWidgets.QVBoxLayout(self.inquiry_widget)
        inquiry_layout.setContentsMargins(8, 8, 8, 8)
        inquiry_layout.setSpacing(6)

        # Message Categories header
        self.label_header1 = QtWidgets.QLabel("Message Categories")
        self.label_header1.setFont(QtGui.QFont("Arial", 14))
        inquiry_layout.addWidget(self.label_header1)

        # Separator
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        inquiry_layout.addWidget(self.line)

        # Filter buttons
        filter_layout = QtWidgets.QVBoxLayout()
        button_style = """
            QPushButton {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                text-align: left;
                padding: 6px 10px;
                margin: 1px 0px;
            }
            QPushButton:hover {
                background-color: #005a2e;
                color: white;
            }
            QPushButton:pressed {
                background-color: #002d17;
            }
        """
        
        self.push_all = QtWidgets.QPushButton("All Messages")
        self.push_all.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_all)

        self.push_unread = QtWidgets.QPushButton("Unread")
        self.push_unread.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_unread)

        self.push_acadin = QtWidgets.QPushButton("Academic Inquiries")
        self.push_acadin.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_acadin)

        self.push_assgt = QtWidgets.QPushButton("Assignment Help")
        self.push_assgt.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_assgt)

        self.push_office = QtWidgets.QPushButton("Office Hours")
        self.push_office.setStyleSheet(button_style)
        filter_layout.addWidget(self.push_office)

        inquiry_layout.addLayout(filter_layout)

        # Separator
        self.line_2 = QtWidgets.QFrame()
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        inquiry_layout.addWidget(self.line_2)

        # Quick Actions
        self.label_actions = QtWidgets.QLabel("Quick Actions")
        self.label_actions.setFont(QtGui.QFont("Arial", 12))
        inquiry_layout.addWidget(self.label_actions)

        self.push_compose = QtWidgets.QPushButton("Compose Message")
        self.push_compose.setStyleSheet("""
            QPushButton {
                color: black;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                text-align: left;
                padding: 6px 10px;
                margin: 1px 0px;
            }
            QPushButton:hover {
                background-color: #005a2e;
                color: white;
            }
            QPushButton:pressed {
                background-color: #002d17;
            }
        """)
        inquiry_layout.addWidget(self.push_compose)

        inquiry_layout.addStretch()
        faculty_layout.addWidget(self.inquiry_widget)

        # ===== Center Panel - Search and Messages =====
        center_widget = QtWidgets.QWidget()
        center_layout = QtWidgets.QVBoxLayout(center_widget)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(8)

        # Search and filter bar
        self.chat_info = QtWidgets.QWidget()
        self.chat_info.setStyleSheet("""
            QWidget#chat_info {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)
        self.chat_info.setObjectName("chat_info")

        search_layout = QtWidgets.QHBoxLayout(self.chat_info)
        search_layout.setContentsMargins(8, 8, 8, 8)

        # Search box
        self.lineEdit_faculty = QtWidgets.QLineEdit()
        self.lineEdit_faculty.setPlaceholderText("Search messages...")
        self.lineEdit_faculty.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                border: 1px solid #ccc;
                padding: 5px 7px;
                font-size: 14px;
                color: #333;
            }
            QLineEdit:focus {
                border: 1px solid #084924;
            }
            QLineEdit:hover {
                border: 1px solid #888;
                background-color: #e9e9e9;
            }
        """)
        search_layout.addWidget(self.lineEdit_faculty)

        # Priority filter
        self.comboBox_prio = QtWidgets.QComboBox()
        self.comboBox_prio.addItems(["All Priorities", "Urgent", "High", "Normal"])
        self.comboBox_prio.setStyleSheet("""
            QComboBox {
                background-color: #f7f7f7;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
                color: #333;
            }
            QComboBox:hover {
                border: 1px solid #888;
                background-color: #e9e9e9;
            }
            QComboBox:focus {
                border: 1px solid #084924;
            }
        """)
        search_layout.addWidget(self.comboBox_prio)

        # Status filter
        self.comboBox_stat = QtWidgets.QComboBox()
        self.comboBox_stat.addItems(["All Status", "Pending", "Sent", "Resolved"])
        self.comboBox_stat.setStyleSheet("""
            QComboBox {
                background-color: #f7f7f7;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                font-size: 14px;
                color: #333;
            }
            QComboBox:hover {
                border: 1px solid #888;
                background-color: #e9e9e9;
            }
            QComboBox:focus {
                border: 1px solid #084924;
            }
        """)
        search_layout.addWidget(self.comboBox_stat)

        center_layout.addWidget(self.chat_info)

        # Messages area
        self.message_widget = QtWidgets.QWidget()
        self.message_widget.setStyleSheet("""
            QWidget#message_widget {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e0e0e0;
                padding: 10px;
            }
        """)
        self.message_widget.setObjectName("message_widget")

        message_layout = QtWidgets.QVBoxLayout(self.message_widget)
        message_layout.setContentsMargins(8, 8, 8, 8)

        # Messages header
        self.label_header1_4 = QtWidgets.QLabel("Recent Messages")
        self.label_header1_4.setFont(QtGui.QFont("Arial", 14))
        message_layout.addWidget(self.label_header1_4)

        # Separator
        self.line_7 = QtWidgets.QFrame()
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        message_layout.addWidget(self.line_7)

        center_layout.addWidget(self.message_widget)
        faculty_layout.addWidget(center_widget, stretch=1)

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


class FacultyApp(QtWidgets.QMainWindow):
    """
    Main faculty application window.
    
    This is like a specialized dashboard for teachers to manage
    all their student communications and inquiries.
    """
    
    def __init__(self):
        super().__init__()
        
        # Initialize data manager for handling all data operations
        self.data_manager = DataManager()
        
        # Set current faculty user (you can change this to any faculty ID from dummy_data.json)
        self.current_faculty_id = 2  # Dr. Maria Santos
        
        # Create the main UI
        self.ui = FacultyMainUI()
        self.setCentralWidget(self.ui)
        
        # Create and add sidebar
        self.sidebar = Sidebar()
        self.ui.add_sidebar(self.sidebar)
        
        # Connect sidebar toggle button to update container width
        self.sidebar.toggle_btn.clicked.connect(self.on_sidebar_toggle)
        
        # Connect header actions
        self.connect_header_actions()
        
        # Connect all the buttons and widgets
        self.connect_buttons()
        
        # Load real data from database
        self.load_faculty_data()
        self.load_messages()
        
        # Set window properties
        self.setWindowTitle("Faculty Messaging Center - CISC Virtual Hub")
        self.setMinimumSize(1980, 1080)
    
    def connect_buttons(self):
        """Connect all buttons to their respective functions"""
        # Filter buttons
        self.ui.push_all.clicked.connect(lambda: self.filter_messages("all"))
        self.ui.push_unread.clicked.connect(lambda: self.filter_messages("unread"))
        self.ui.push_acadin.clicked.connect(lambda: self.filter_messages("academic"))
        self.ui.push_assgt.clicked.connect(lambda: self.filter_messages("assignment"))
        self.ui.push_office.clicked.connect(lambda: self.filter_messages("office"))
        
        # Compose button
        self.ui.push_compose.clicked.connect(self.compose_message)
        
        # Filter combo boxes
        self.ui.comboBox_prio.currentTextChanged.connect(self.apply_filters)
        self.ui.comboBox_stat.currentTextChanged.connect(self.apply_filters)
        
        # Search functionality
        self.ui.lineEdit_faculty.textChanged.connect(self.search_messages)
    
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
    
    def on_sidebar_toggle(self):
        """Handle sidebar toggle - check if sidebar is collapsed"""
        # The sidebar's is_collapsed state gets updated in toggleDrawer
        # We need to check it after the toggle happens
        # Use QTimer to check state after the toggle completes
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(50, self.update_sidebar_container)
    
    def update_sidebar_container(self):
        """Update the sidebar container width based on sidebar's current state"""
        self.ui.update_sidebar_width(self.sidebar.is_collapsed)
    
    def load_faculty_data(self):
        """Load current faculty information"""
        faculty = self.data_manager.get_user(self.current_faculty_id)
        if faculty:
            print(f"Faculty logged in: {faculty['name']} ({faculty['department']})")
            # You can update the UI to show faculty name if needed
    
    def load_messages(self):
        """Load all messages and inquiries for the current faculty member"""
        # Get all messages where this faculty is the receiver
        faculty_messages = []
        for message in self.data_manager.data['messages']:
            if message.get('receiver_id') == self.current_faculty_id:
                faculty_messages.append(message)
        
        # Get all inquiries assigned to this faculty
        faculty_inquiries = self.data_manager.get_inquiries_by_faculty(self.current_faculty_id)
        
        # Combine and sort by date
        all_items = []
        
        # Add messages
        for msg in faculty_messages:
            sender = self.data_manager.get_user(msg.get('sender_id'))
            all_items.append({
                'type': 'message',
                'id': msg['id'],
                'title': msg.get('subject', 'No Subject'),
                'content': msg.get('content', ''),
                'sender': sender['name'] if sender else 'Unknown',
                'priority': msg.get('priority', 'normal'),
                'status': msg.get('status', 'pending'),
                'date': msg.get('created_at', ''),
                'is_read': msg.get('is_read', False)
            })
        
        # Add inquiries
        for inquiry in faculty_inquiries:
            student = self.data_manager.get_user(inquiry.get('student_id'))
            all_items.append({
                'type': 'inquiry',
                'id': inquiry['id'],
                'title': inquiry.get('subject', 'No Subject'),
                'content': inquiry.get('description', ''),
                'sender': student['name'] if student else 'Unknown',
                'priority': inquiry.get('priority', 'normal'),
                'status': inquiry.get('status', 'pending'),
                'date': inquiry.get('created_at', ''),
                'is_read': True  # Inquiries are always considered "read" when assigned
            })
        
        # Sort by date (most recent first)
        all_items.sort(key=lambda x: x['date'], reverse=True)
        
        # Store for filtering
        self.all_items = all_items
        self.filtered_items = all_items.copy()
        
        # Display items
        self.display_items()
    
    def display_items(self):
        """Display the filtered items in the message widget"""
        # Clear existing content
        for child in self.ui.message_widget.findChildren(QtWidgets.QWidget):
            if child != self.ui.label_header1_4 and child != self.ui.line_7:
                child.deleteLater()
        
        if not self.filtered_items:
            # Show "no messages" message
            no_msg_label = QtWidgets.QLabel("No messages found!")
            no_msg_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            no_msg_label.setStyleSheet("font-size: 16px; color: #666; margin: 50px;")
            no_msg_label.setParent(self.ui.message_widget)
            no_msg_label.move(250, 300)
            no_msg_label.show()
            return
        
        # Create scroll area for messages
        scroll_area = QtWidgets.QScrollArea(self.ui.message_widget)
        scroll_area.setGeometry(8, 50, 700, 650)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Create content widget
        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QVBoxLayout(content_widget)
        content_layout.setContentsMargins(5, 5, 5, 5)
        content_layout.setSpacing(10)
        
        # Add message cards
        for item in self.filtered_items:
            card = self.create_message_card(item)
            content_layout.addWidget(card)
        
        scroll_area.setWidget(content_widget)
        scroll_area.show()
    
    def create_message_card(self, item):
        """Create a message card widget for displaying individual messages"""
        card = QtWidgets.QFrame()
        card.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel)
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 10px;
                margin: 2px;
            }
            QFrame:hover {
                border: 1px solid #084924;
                background-color: #f8f9fa;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout(card)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
        
        # Header with sender name and status
        header_layout = QtWidgets.QHBoxLayout()
        
        # Sender name
        sender_label = QtWidgets.QLabel(item['sender'])
        sender_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #084924;")
        header_layout.addWidget(sender_label)
        
        header_layout.addStretch()
        
        # Status badge
        status = item['status']
        status_color = {
            'pending': '#fbbf24',
            'sent': '#10b981', 
            'resolved': '#6b7280',
            'in_progress': '#3b82f6'
        }.get(status, '#6b7280')
        
        status_label = QtWidgets.QLabel(status.upper())
        status_label.setStyleSheet(f"""
            background-color: {status_color};
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: bold;
        """)
        header_layout.addWidget(status_label)
        
        layout.addLayout(header_layout)
        
        # Title
        title_label = QtWidgets.QLabel(item['title'])
        title_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #333;")
        title_label.setWordWrap(True)
        layout.addWidget(title_label)
        
        # Content preview
        content_preview = item['content'][:100] + "..." if len(item['content']) > 100 else item['content']
        content_label = QtWidgets.QLabel(content_preview)
        content_label.setStyleSheet("font-size: 12px; color: #666;")
        content_label.setWordWrap(True)
        layout.addWidget(content_label)
        
        # Footer with date and priority
        footer_layout = QtWidgets.QHBoxLayout()
        
        # Date
        date_text = item['date'][:10] if item['date'] else 'Unknown'
        date_label = QtWidgets.QLabel(date_text)
        date_label.setStyleSheet("font-size: 10px; color: #999;")
        footer_layout.addWidget(date_label)
        
        footer_layout.addStretch()
        
        # Priority
        priority = item['priority']
        priority_color = {
            'urgent': '#ef4444',
            'high': '#f59e0b',
            'normal': '#6b7280'
        }.get(priority, '#6b7280')
        
        priority_label = QtWidgets.QLabel(priority.upper())
        priority_label.setStyleSheet(f"""
            color: {priority_color};
            font-size: 10px;
            font-weight: bold;
        """)
        footer_layout.addWidget(priority_label)
        
        layout.addLayout(footer_layout)
        
        # Make card clickable
        card.mousePressEvent = lambda event, item=item: self.on_message_clicked(item)
        
        return card
    
    def on_message_clicked(self, item):
        """Handle when a message card is clicked"""
        print(f"Clicked on {item['type']}: {item['title']}")
        
        # Mark as read if it's a message
        if item['type'] == 'message':
            self.data_manager.update_message(item['id'], {'is_read': True})
        
        # Show detailed view (you can implement this later)
        QtWidgets.QMessageBox.information(
            self, 
            f"{item['type'].title()} Details",
            f"Title: {item['title']}\n\n"
            f"From: {item['sender']}\n"
            f"Priority: {item['priority']}\n"
            f"Status: {item['status']}\n\n"
            f"Content:\n{item['content']}"
        )
    
    def filter_messages(self, filter_type):
        """Filter messages based on category"""
        print(f"Filtering by: {filter_type}")
        
        if filter_type == "all":
            self.filtered_items = self.all_items.copy()
        elif filter_type == "unread":
            self.filtered_items = [item for item in self.all_items if not item.get('is_read', True)]
        elif filter_type == "academic":
            self.filtered_items = [item for item in self.all_items if item['type'] == 'inquiry']
        elif filter_type == "assignment":
            # Filter for assignment-related messages (you can enhance this)
            self.filtered_items = [item for item in self.all_items if 'assignment' in item['title'].lower()]
        elif filter_type == "office":
            # Filter for office hours related messages (you can enhance this)
            self.filtered_items = [item for item in self.all_items if 'office' in item['title'].lower()]
        
        self.display_items()
    
    def apply_filters(self):
        """Apply priority and status filters"""
        priority_filter = self.ui.comboBox_prio.currentText()
        status_filter = self.ui.comboBox_stat.currentText()
        
        filtered = self.filtered_items.copy()
        
        # Apply priority filter
        if priority_filter != "All Priorities":
            priority_map = {
                "Urgent": "urgent",
                "High": "high", 
                "Normal": "normal"
            }
            if priority_filter in priority_map:
                filtered = [item for item in filtered if item['priority'] == priority_map[priority_filter]]
        
        # Apply status filter
        if status_filter != "All Status":
            status_map = {
                "Pending": "pending",
                "Sent": "sent",
                "Resolved": "resolved"
            }
            if status_filter in status_map:
                filtered = [item for item in filtered if item['status'] == status_map[status_filter]]
        
        self.filtered_items = filtered
        self.display_items()
    
    def search_messages(self, search_text):
        """Search messages by content"""
        if not search_text.strip():
            self.filtered_items = self.all_items.copy()
        else:
            search_lower = search_text.lower()
            self.filtered_items = [
                item for item in self.all_items 
                if (search_lower in item['title'].lower() or 
                    search_lower in item['content'].lower() or
                    search_lower in item['sender'].lower())
            ]
        
        self.display_items()
    
    def compose_message(self):
        """Open compose message dialog"""
        print("Opening compose message dialog...")
        # You can implement a compose message dialog here
        QtWidgets.QMessageBox.information(self, "Compose Message", "Compose message feature coming soon!")


def main():
    """Main function to run the faculty application"""
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
    
    # Create and show the faculty application
    window = FacultyApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
