"""
CISC Virtual Hub Launcher
=========================

This is the main launcher for the CISC Virtual Hub messaging system.
It allows users to choose between student and faculty interfaces.

This is like a main menu where you can choose which part of the system to use.
"""

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from msg_main import MainApp
from faculty_app import FacultyApp


class LauncherDialog(QtWidgets.QDialog):
    """
    Main launcher dialog for choosing between student and faculty interfaces.
    
    This is like a welcome screen where you choose your role in the system.
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CISC Virtual Hub - Welcome")
        self.setFixedSize(600, 400)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        
        # Set up the UI
        self.setup_ui()
        
        # Connect buttons
        self.student_btn.clicked.connect(self.launch_student_app)
        self.faculty_btn.clicked.connect(self.launch_faculty_app)
        self.exit_btn.clicked.connect(self.close)
    
    def setup_ui(self):
        """Set up the launcher user interface"""
        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        # Header
        header_layout = QtWidgets.QVBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Logo and title
        title_label = QtWidgets.QLabel("CISC Virtual Hub")
        title_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #084924;
            margin-bottom: 10px;
        """)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(title_label)
        
        subtitle_label = QtWidgets.QLabel("Messaging System")
        subtitle_label.setStyleSheet("""
            font-size: 16px;
            color: #666;
            margin-bottom: 20px;
        """)
        subtitle_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(subtitle_label)
        
        main_layout.addLayout(header_layout)
        
        # Role selection
        role_layout = QtWidgets.QVBoxLayout()
        role_layout.setSpacing(15)
        
        # Student button
        self.student_btn = QtWidgets.QPushButton("👨‍🎓 Student Portal")
        self.student_btn.setStyleSheet("""
            QPushButton {
                background-color: #084924;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 20px;
                border: none;
                border-radius: 10px;
                min-height: 60px;
            }
            QPushButton:hover {
                background-color: #005a2e;
            }
            QPushButton:pressed {
                background-color: #002d17;
            }
        """)
        role_layout.addWidget(self.student_btn)
        
        # Faculty button
        self.faculty_btn = QtWidgets.QPushButton("👨‍🏫 Faculty Portal")
        self.faculty_btn.setStyleSheet("""
            QPushButton {
                background-color: #1e4d2b;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 20px;
                border: none;
                border-radius: 10px;
                min-height: 60px;
            }
            QPushButton:hover {
                background-color: #2d5a3d;
            }
            QPushButton:pressed {
                background-color: #0f2a15;
            }
        """)
        role_layout.addWidget(self.faculty_btn)
        
        main_layout.addLayout(role_layout)
        
        # Description
        desc_label = QtWidgets.QLabel(
            "Choose your role to access the appropriate messaging interface.\n"
            "Students can create inquiries and communicate with faculty.\n"
            "Faculty can manage messages, inquiries, and respond to students."
        )
        desc_label.setStyleSheet("""
            font-size: 12px;
            color: #666;
            text-align: center;
            margin: 20px 0;
        """)
        desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        desc_label.setWordWrap(True)
        main_layout.addWidget(desc_label)
        
        # Exit button
        self.exit_btn = QtWidgets.QPushButton("Exit")
        self.exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #6b7280;
                color: white;
                font-size: 14px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #4b5563;
            }
            QPushButton:pressed {
                background-color: #374151;
            }
        """)
        main_layout.addWidget(self.exit_btn)
        
        # Set background
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
                border: 2px solid #e0e0e0;
                border-radius: 15px;
            }
        """)
    
    def launch_student_app(self):
        """Launch the student messaging application"""
        print("Launching Student Portal...")
        self.hide()  # Hide the launcher
        
        # Create and show student app
        self.student_app = MainApp()
        self.student_app.show()
        
        # Connect the student app's close event to show launcher again
        self.student_app.closeEvent = lambda event: self.show_launcher_after_close(event, self.student_app)
    
    def launch_faculty_app(self):
        """Launch the faculty messaging application"""
        print("Launching Faculty Portal...")
        self.hide()  # Hide the launcher
        
        # Create and show faculty app
        self.faculty_app = FacultyApp()
        self.faculty_app.show()
        
        # Connect the faculty app's close event to show launcher again
        self.faculty_app.closeEvent = lambda event: self.show_launcher_after_close(event, self.faculty_app)
    
    def show_launcher_after_close(self, event, app):
        """Show the launcher again after an app is closed"""
        app.closeEvent = None  # Remove the custom close event
        app.close()  # Close the app
        self.show()  # Show the launcher again


def main():
    """Main function to run the launcher"""
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
    
    # Create and show the launcher
    launcher = LauncherDialog()
    launcher.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
