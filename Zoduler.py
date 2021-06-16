from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from datetime import datetime
import threading
import time
import pyautogui
import webbrowser
import sys
sys.dont_write_bytecode = True


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 552)
        MainWindow.setMaximumSize(410, 552)
        MainWindow.setMinimumSize(410, 552)
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Bin/icons/iconmain.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(10, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.topic_label = QtWidgets.QLabel(self.centralwidget)
        self.topic_label.setGeometry(QtCore.QRect(10, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.topic_label.setFont(font)
        self.topic_label.setObjectName("topic_label")
        self.meeting_topic = QtWidgets.QLineEdit(self.centralwidget)
        self.meeting_topic.setGeometry(QtCore.QRect(10, 90, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_topic.setFont(font)
        self.meeting_topic.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.meeting_topic.setStyleSheet("border: 0.5px solid rgb(38, 129, 242) ;\n"
                                         "border-radius: 4px")
        self.meeting_topic.setInputMask("")
        self.meeting_topic.setMaxLength(50)
        self.meeting_topic.setFrame(True)
        self.meeting_topic.setCursorPosition(0)
        self.meeting_topic.setClearButtonEnabled(True)
        self.meeting_topic.setObjectName("meeting_topic")
        self.meeting_id_label = QtWidgets.QLabel(self.centralwidget)
        self.meeting_id_label.setGeometry(QtCore.QRect(10, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_id_label.setFont(font)
        self.meeting_id_label.setObjectName("meeting_id_label")
        self.passcode_label = QtWidgets.QLabel(self.centralwidget)
        self.passcode_label.setGeometry(QtCore.QRect(10, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.passcode_label.setFont(font)
        self.passcode_label.setObjectName("passcode_label")
        self.meeting_id = QtWidgets.QLineEdit(self.centralwidget)
        self.meeting_id.setGeometry(QtCore.QRect(10, 170, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_id.setFont(font)
        self.meeting_id.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.meeting_id.setStyleSheet("border: 0.5px solid rgb(38, 129, 242) ;\n"
                                      "border-radius: 4px")
        self.meeting_id.setInputMask("")
        self.meeting_id.setMaxLength(11)
        self.meeting_id.setFrame(True)
        self.meeting_id.setCursorPosition(0)
        self.meeting_id.setClearButtonEnabled(True)
        self.meeting_id.setObjectName("meeting_id")
        self.meeting_passcode = QtWidgets.QLineEdit(self.centralwidget)
        self.meeting_passcode.setGeometry(QtCore.QRect(10, 250, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.meeting_passcode.setFont(font)
        self.meeting_passcode.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.meeting_passcode.setStyleSheet("border: 0.5px solid rgb(38, 129, 242) ;\n"
                                            "border-radius: 4px")
        self.meeting_passcode.setInputMask("")
        self.meeting_passcode.setMaxLength(50)
        self.meeting_passcode.setFrame(True)
        self.meeting_passcode.setCursorPosition(0)
        self.meeting_passcode.setClearButtonEnabled(True)
        self.meeting_passcode.setObjectName("meeting_passcode")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(10, 310, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.duration_label = QtWidgets.QLabel(self.centralwidget)
        self.duration_label.setGeometry(QtCore.QRect(10, 350, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.duration_label.setFont(font)
        self.duration_label.setObjectName("duration_label")
        self.time = QtWidgets.QTimeEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(100, 310, 301, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.time.setFont(font)
        self.time.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.time.setObjectName("time")
        self.duration = QtWidgets.QComboBox(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(100, 350, 301, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.duration.setFont(font)
        self.duration.setStyleSheet("")
        self.duration.setObjectName("duration")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.duration.addItem("")
        self.recurring_meeting = QtWidgets.QCheckBox(self.centralwidget)
        self.recurring_meeting.setGeometry(QtCore.QRect(10, 390, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.recurring_meeting.setFont(font)
        self.recurring_meeting.setFocusPolicy(QtCore.Qt.NoFocus)
        self.recurring_meeting.setStyleSheet(
            "border: 0.5 px solid rgb(38, 129, 242);")
        self.recurring_meeting.setObjectName("recurring_meeting")
        self.divider = QtWidgets.QFrame(self.centralwidget)
        self.divider.setEnabled(True)
        self.divider.setGeometry(QtCore.QRect(10, 280, 391, 31))
        self.divider.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider.setObjectName("divider")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(10, 420, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background-color: rgb(38, 129, 242);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 4px\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "")
        self.save_btn.setFlat(False)
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.on_click)
        self.scheduled = QtWidgets.QGroupBox(self.centralwidget)
        self.scheduled.setGeometry(QtCore.QRect(10, 460, 391, 80))
        self.scheduled.setObjectName("scheduled")
        self.schedule_id = QtWidgets.QLabel(self.scheduled)
        self.schedule_id.setGeometry(QtCore.QRect(10, 50, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_id.setFont(font)
        self.schedule_id.setObjectName("schedule_id")
        self.schedule_topic = QtWidgets.QLabel(self.scheduled)
        self.schedule_topic.setGeometry(QtCore.QRect(10, 20, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_topic.setFont(font)
        self.schedule_topic.setObjectName("schedule_topic")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(380, 10, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.info.setFont(font)
        self.info.setStyleSheet("border: 1px solid rgb(38, 129, 242);\n"
                                "border-radius: 5px")
        self.info.setObjectName("info")
        self.info.clicked.connect(self.info_btn)
        self.import_2 = QtWidgets.QPushButton(self.centralwidget)
        self.import_2.setGeometry(QtCore.QRect(350, 10, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.import_2.setFont(font)
        self.import_2.setStyleSheet("border: 1px solid rgb(38, 129, 242);\n"
                                    "border-radius: 5px")
        self.import_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Bin/icons/import.ico"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_2.setIcon(icon1)
        self.import_2.setObjectName("import_2")
        self.import_2.clicked.connect(self.import_save)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def recorder(self):
        if recfor == 'For 10 minutes':
            rec_time = 10 * 60
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(rec_time)
            pyautogui.hotkey('win', 'alt', 'r')
            app.exit()

        if recfor == 'For 15 minutes':
            rec_time = 15 * 60
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(rec_time)
            pyautogui.hotkey('win', 'alt', 'r')
            app.exit()

        if recfor == 'For 30 minutes':
            rec_time = 30 * 60
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(rec_time)
            pyautogui.hotkey('win', 'alt', 'r')
            app.exit()

        if recfor == 'For 45 minutes':
            rec_time = 45 * 60
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(rec_time)
            pyautogui.hotkey('win', 'alt', 'r')
            app.exit()

        if recfor == 'For 60 minutes':
            rec_time = 60 * 60
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(rec_time)
            pyautogui.hotkey('win', 'alt', 'r')
            app.exit()

        if recfor == 'For 90 minutes':
            rec_time = 90 * 60
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(rec_time)
            pyautogui.hotkey('win', 'alt', 'r')
            app.exit()

    def on_click(self):
        global topictolist
        global meeting_id_final
        global password_final
        global time_hour
        global time_minute
        global final_time
        global scheduled_id_final
        global scheduled_topic_final
        global scheduled_passcode
        scheduled_id_final = self.meeting_id.text()
        scheduled_topic_final = self.meeting_topic.text()
        scheduled_passcode = self.meeting_passcode.text()
        _id = f'Meeting ID:         {scheduled_id_final}'
        _topic = f'Meeting Topic:     {scheduled_topic_final}'
        self.schedule_id.setText(_id)
        self.schedule_topic.setText(_topic)
        self.save_btn.setEnabled(False)
        self.meeting_topic.setEnabled(False)
        self.meeting_id.setEnabled(False)
        self.meeting_passcode.setEnabled(False)
        if self.recurring_meeting.isChecked():
            self.save_recurr()
        time_hour = str(self.time.time().hour())
        time_minute = str(self.time.time().minute())
        final_time = time_hour + ':' + time_minute
        threading.Thread(target=self.executer).start()

    def executer(self):
        while True:
            now = datetime.now()
            current_time = now.strftime('%H:%M')
            if final_time == current_time:
                threading.Thread(target=self.clicker).start()
                break

    def clicker(self):
        global recfor
        pyautogui.press('win')
        pyautogui.write('Zoom')
        pyautogui.press('enter')
        join_btn = None
        while True:
            if join_btn == None:
                join_btn = pyautogui.locateOnScreen(
                    "Bin/icons/zoom_btn.png", grayscale=True, confidence=0.6)

            if join_btn != None:
                pyautogui.click(join_btn)
                time.sleep(5)
                pyautogui.write(scheduled_id_final, interval=0.25)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.write(scheduled_passcode, interval=0.25)
                pyautogui.press('enter')
                time.sleep(5)
                recfor = self.duration.currentText()
                threading.Thread(target=self.recorder).start()

    def save_recurr(self):
        filename = 'Bin/Recurring Meetings/' + scheduled_topic_final + '.zods'
        f = open(filename, 'a')
        f.write(scheduled_topic_final + '\n' +
                scheduled_id_final + '\n' + scheduled_passcode)
        f.close()

    def import_save(self):
        try:
            saved_file = QFileDialog.getOpenFileName(
                None, 'Select File', "", "ZODS (*.zods)")
            file = saved_file[0]
            r = open(file, 'rt')
            line_1 = r.readline().strip()
            line_2 = r.readline().strip()
            line_3 = r.readline().strip()
            self.meeting_topic.setText(line_1)
            self.meeting_id.setText(line_2)
            self.meeting_passcode.setText(line_3)
            r.close()
        except:
            pass

    def info_btn(self):
        webbrowser.open('https://github.com/AribMuhtasim21/zoduler')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zoduler"))
        self.title.setText(_translate("MainWindow", "Schedule a meeting"))
        self.topic_label.setText(_translate("MainWindow", "Topic"))
        self.meeting_topic.setPlaceholderText(
            _translate("MainWindow", "Meeting\'s topic"))
        self.meeting_id_label.setText(_translate("MainWindow", "Meeting ID"))
        self.passcode_label.setText(_translate("MainWindow", "Passcode"))
        self.meeting_id.setPlaceholderText(
            _translate("MainWindow", "Meeting ID"))
        self.meeting_passcode.setPlaceholderText(
            _translate("MainWindow", "Meeting Passcode"))
        self.time_label.setText(_translate("MainWindow", "Time:"))
        self.duration_label.setText(_translate("MainWindow", "Duration:"))
        self.duration.setItemText(0, _translate("MainWindow", "0 minutes"))
        self.duration.setItemText(1, _translate("MainWindow", "15 minutes"))
        self.duration.setItemText(2, _translate("MainWindow", "30 minutes"))
        self.duration.setItemText(3, _translate("MainWindow", "45 minutes"))
        self.duration.setItemText(4, _translate("MainWindow", "60 minutes"))
        self.duration.setItemText(5, _translate("MainWindow", "90 minutes"))
        self.recurring_meeting.setText(
            _translate("MainWindow", "Recurring Meeting"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.scheduled.setTitle(_translate("MainWindow", "Scheduled Meeting"))
        self.schedule_id.setText(_translate(
            "MainWindow", "Meeting  ID:         None"))
        self.schedule_topic.setText(_translate(
            "MainWindow", "Meeting Topic:     None"))
        self.info.setText(_translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
