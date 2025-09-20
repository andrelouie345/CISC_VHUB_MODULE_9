from PyQt6 import QtCore, QtWidgets
from recipient_dialog import Ui_Form   # generated from recipient_dialog.ui


# ============================
# Inquiry Dialog UI Class
# ============================
class Ui_InquiryDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("InquiryDialog")
        Dialog.resize(420, 500)

        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(Dialog)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        self.main_layout.setSpacing(10)

        # White container (styled card)
        self.inquiry_widget = QtWidgets.QWidget(parent=Dialog)
        self.inquiry_widget.setObjectName("inquiry_widget")
        self.inquiry_widget.setStyleSheet("""
            QWidget#inquiry_widget {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #dddddd;
            }
        """)

        # Form layout
        self.form_layout = QtWidgets.QVBoxLayout(self.inquiry_widget)
        self.form_layout.setContentsMargins(20, 20, 20, 20)
        self.form_layout.setSpacing(12)

        # Title
        self.inquiry_header = QtWidgets.QLabel("New Inquiry")
        self.inquiry_header.setStyleSheet("color: #084924; font-size: 20px; font-weight: bold;")
        self.form_layout.addWidget(self.inquiry_header)

        # Inquiry Type Buttons
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
        self.form_layout.addWidget(self.label_to)

        self.recipient_layout = QtWidgets.QHBoxLayout()
        self.search_recipt = QtWidgets.QLineEdit()
        self.search_recipt.setPlaceholderText("Enter recipient...")

        # ✅ Use one consistent button name
        self.btn_select_recipient = QtWidgets.QPushButton("△")
        self.btn_select_recipient.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #003d1f;
                border: none;
                font-size: 20px;
            }
            QPushButton:hover {
                color: #005a2e;
            }
            QPushButton:pressed {
                color: #002d17;
            }
        """)
        self.btn_select_recipient.setToolTip("Select Recipient")

        self.recipient_layout.addWidget(self.search_recipt)
        self.recipient_layout.addWidget(self.btn_select_recipient)
        self.form_layout.addLayout(self.recipient_layout)

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

        # Info Note
        self.label_note = QtWidgets.QLabel(
            "Be as specific as possible to help us provide the best assistance."
        )
        self.label_note.setWordWrap(True)
        self.label_note.setStyleSheet("font-size: 11px; color: gray;")
        self.form_layout.addWidget(self.label_note)

        # Additional Options
        self.label_opts = QtWidgets.QLabel("Additional Options")
        self.checkBox_4 = QtWidgets.QCheckBox("Request read receipt")
        self.checkBox_5 = QtWidgets.QCheckBox("Send copy to my email")
        self.checkBox_6 = QtWidgets.QCheckBox("Mark as confidential")
        self.form_layout.addWidget(self.label_opts)
        self.form_layout.addWidget(self.checkBox_4)
        self.form_layout.addWidget(self.checkBox_5)
        self.form_layout.addWidget(self.checkBox_6)

        # Bottom Buttons (Cancel / Create)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_cancel = QtWidgets.QPushButton("Cancel")
        self.button_create = QtWidgets.QPushButton("Create")
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.button_cancel)
        self.button_layout.addWidget(self.button_create)
        self.form_layout.addLayout(self.button_layout)

        # Add the form card to the main layout
        self.main_layout.addWidget(self.inquiry_widget)


# ============================
# Inquiry Dialog Wrapper
# ============================
class InquiryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InquiryDialog()
        self.ui.setupUi(self)

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(420, 500)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.Dialog
        )

        # Connect buttons
        self.ui.button_cancel.clicked.connect(self.reject)
        self.ui.button_create.clicked.connect(self.accept)

        # ✅ Connect recipient selector button
        self.ui.btn_select_recipient.clicked.connect(self.open_recipient_dialog)

    def open_recipient_dialog(self):
        """Function to open the recipient selection dialog"""
        dialog = QtWidgets.QDialog(self)   # real dialog
        ui = Ui_Form()                     # load recipient form
        ui.setupUi(dialog)                 # set it up

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(420, 500)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.Dialog
        )

        if dialog.exec():
            print("Recipient Selected!")
            # TODO: extract selected recipient from ui → put in self.ui.search_recipt.setText(...)
        else:
            print("Recipient Selection Cancelled")
