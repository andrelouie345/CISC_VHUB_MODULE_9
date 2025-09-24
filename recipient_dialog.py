from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 385)

        # Make the window borderless
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.header_widget = QtWidgets.QWidget(parent=Form)
        self.header_widget.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.header_widget.setStyleSheet("QWidget#header_widget {\n"
                                         "    background-color: #084924; /* Dark green */\n"
                                         "    color: white;\n"
                                         "    padding: 10px;\n"
                                         "    font-size: 16px;\n"
                                         "    font-family: \"Poppins\";\n"
                                         "}")
        self.header_widget.setObjectName("header_widget")

        self.recipient_label = QtWidgets.QLabel(parent=self.header_widget)
        self.recipient_label.setGeometry(QtCore.QRect(10, -10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.recipient_label.setFont(font)
        self.recipient_label.setStyleSheet("QLabel#recipient_label {\n"
                                           "    color: white\n"
                                           "}")
        self.recipient_label.setObjectName("recipient_label")

        self.recipient_search = QtWidgets.QLineEdit(parent=Form)
        self.recipient_search.setGeometry(QtCore.QRect(10, 50, 371, 31))
        self.recipient_search.setStyleSheet("QLineEdit#recipient_search {\n"
                                            "    border: 1px solid #ccc;\n"
                                            "    font-family: \"Segoe UI\", sans-serif;\n"
                                            "}")
        


        self.recipient_search.setObjectName("recipient_search")
        self.recipients = ["Alice", "Bob", "Charlie", "Diana", "Eve","Dion","Earl"]


        completer = QtWidgets.QCompleter(self.recipients, self.recipient_search)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.recipient_search.setCompleter(completer)

        self.widget_selector = QtWidgets.QWidget(parent=Form)
        self.widget_selector.setGeometry(QtCore.QRect(10, 80, 371, 281))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.widget_selector.setFont(font)
        self.widget_selector.setStyleSheet("QWidget#widget_selector {\n"
                                           "    background-color: white;\n"
                                           "    border: 1px solid #ccc;\n"
                                           "    font-family: \"Segoe UI\", sans-serif;\n"
                                           "}")
        self.widget_selector.setObjectName("widget_selector")

        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.widget_selector)
        self.buttonBox.setGeometry(QtCore.QRect(210, 250, 156, 24))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel |
                                          QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # Connect OK and Cancel
        self.buttonBox.accepted.connect(Form.accept)  # OK button
        self.buttonBox.rejected.connect(Form.reject)  # Cancel button

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.recipient_label.setText(_translate("Form", "Select Recipient..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()  # ✅ must be QDialog, not QWidget
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
