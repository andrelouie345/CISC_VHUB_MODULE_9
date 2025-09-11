from PyQt6 import QtCore, QtWidgets


class Ui_InquiryDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("InquiryDialog")
        Dialog.resize(420, 500)

        # Main layout for the dialog
        self.main_layout = QtWidgets.QVBoxLayout(Dialog)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        self.main_layout.setSpacing(10)

        # White container
        self.inquiry_widget = QtWidgets.QWidget(parent=Dialog)
        self.inquiry_widget.setObjectName("inquiry_widget")
        self.inquiry_widget.setStyleSheet("""
            QWidget#inquiry_widget {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #dddddd;
            }
        """)

        # Layout for form inside the white container
        self.form_layout = QtWidgets.QVBoxLayout(self.inquiry_widget)
        self.form_layout.setContentsMargins(20, 20, 20, 20)
        self.form_layout.setSpacing(12)

        # Header
        self.inquiry_header = QtWidgets.QLabel("New Inquiry")
        self.inquiry_header.setStyleSheet("color: #084924; font-size: 20px; font-weight: bold;")
        self.form_layout.addWidget(self.inquiry_header)

        # Inquiry type buttons (grid layout)
        self.type_layout = QtWidgets.QGridLayout()
        self.push_acad = QtWidgets.QPushButton("Academic")
        self.push_admin = QtWidgets.QPushButton("Administrative")
        self.push_tech = QtWidgets.QPushButton("Technical")
        self.push_gen = QtWidgets.QPushButton("General")
        self.type_layout.addWidget(self.push_acad, 0, 0)
        self.type_layout.addWidget(self.push_tech, 0, 1)
        self.type_layout.addWidget(self.push_admin, 1, 0)
        self.type_layout.addWidget(self.push_gen, 1, 1)
        self.form_layout.addLayout(self.type_layout)

        # Recipient
        self.label_to = QtWidgets.QLabel("Send to")
        self.search_recipt = QtWidgets.QLineEdit()
        self.search_recipt.setPlaceholderText("Enter recipient...")
        self.form_layout.addWidget(self.label_to)
        self.form_layout.addWidget(self.search_recipt)

        # Priority
        self.label_priority = QtWidgets.QLabel("Priority Level")
        self.priority_layout = QtWidgets.QHBoxLayout()
        self.checkBox = QtWidgets.QCheckBox("Normal")
        self.checkBox_2 = QtWidgets.QCheckBox("High")
        self.checkBox_3 = QtWidgets.QCheckBox("Urgent")
        self.priority_layout.addWidget(self.checkBox)
        self.priority_layout.addWidget(self.checkBox_2)
        self.priority_layout.addWidget(self.checkBox_3)
        self.form_layout.addWidget(self.label_priority)
        self.form_layout.addLayout(self.priority_layout)

        # Subject
        self.label_sub = QtWidgets.QLabel("Subject")
        self.search_sub = QtWidgets.QLineEdit()
        self.form_layout.addWidget(self.label_sub)
        self.form_layout.addWidget(self.search_sub)

        # Message
        self.label_msg = QtWidgets.QLabel("Detailed message")
        self.search_msg = QtWidgets.QLineEdit()
        self.form_layout.addWidget(self.label_msg)
        self.form_layout.addWidget(self.search_msg)

        # Info note
        self.label_note = QtWidgets.QLabel(
            "Be as specific as possible to help us provide the best assistance."
        )
        self.label_note.setWordWrap(True)
        self.label_note.setStyleSheet("font-size: 11px; color: gray;")
        self.form_layout.addWidget(self.label_note)

        # Options
        self.label_opts = QtWidgets.QLabel("Additional Options")
        self.checkBox_4 = QtWidgets.QCheckBox("Request read receipt")
        self.checkBox_5 = QtWidgets.QCheckBox("Send copy to my email")
        self.checkBox_6 = QtWidgets.QCheckBox("Mark as confidential")
        self.form_layout.addWidget(self.label_opts)
        self.form_layout.addWidget(self.checkBox_4)
        self.form_layout.addWidget(self.checkBox_5)
        self.form_layout.addWidget(self.checkBox_6)

        # Buttons
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_cancel = QtWidgets.QPushButton("Cancel")
        self.button_create = QtWidgets.QPushButton("Create")
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.button_cancel)
        self.button_layout.addWidget(self.button_create)
        self.form_layout.addLayout(self.button_layout)

        # Add the white card to main layout
        self.main_layout.addWidget(self.inquiry_widget)


class InquiryDialog(QtWidgets.QDialog):
    """Wrapper class to use the Inquiry UI as a dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InquiryDialog()
        self.ui.setupUi(self)
        # Make the dialog background transparent
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


        # Make it behave like a real dialog
        self.setFixedSize(420, 500)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(
        QtCore.Qt.WindowType.FramelessWindowHint |
        QtCore.Qt.WindowType.Dialog
)


        # Connect buttons
        self.ui.button_cancel.clicked.connect(self.reject)
        self.ui.button_create.clicked.connect(self.accept)
