# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI-dataLoad.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.error_box = QtWidgets.QGroupBox(self.tab_1)
        self.error_box.setStatusTip("")
        self.error_box.setObjectName("error_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.error_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.error_dropmenu = QtWidgets.QComboBox(self.error_box)
        self.error_dropmenu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error_dropmenu.setObjectName("error_dropmenu")
        self.error_dropmenu.addItem("")
        self.error_dropmenu.addItem("")
        self.error_dropmenu.addItem("")
        self.horizontalLayout_3.addWidget(self.error_dropmenu)
        self.verticalLayout_2.addWidget(self.error_box)
        self.loadfile_box = QtWidgets.QGroupBox(self.tab_1)
        self.loadfile_box.setObjectName("loadfile_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.loadfile_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadfile_input = QtWidgets.QLineEdit(self.loadfile_box)
        self.loadfile_input.setObjectName("loadfile_input")
        self.horizontalLayout.addWidget(self.loadfile_input)
        self.loadfile_btn = QtWidgets.QPushButton(self.loadfile_box)
        self.loadfile_btn.setObjectName("loadfile_btn")
        self.horizontalLayout.addWidget(self.loadfile_btn)
        self.verticalLayout_2.addWidget(self.loadfile_box)
        self.drop_box = QtWidgets.QGroupBox(self.tab_1)
        self.drop_box.setObjectName("drop_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.drop_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.drop_input = QtWidgets.QPlainTextEdit(self.drop_box)
        self.drop_input.setAcceptDrops(True)
        self.drop_input.setOverwriteMode(True)
        self.drop_input.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.drop_input.setBackgroundVisible(True)
        self.drop_input.setCenterOnScroll(True)
        self.drop_input.setObjectName("drop_input")
        self.horizontalLayout_2.addWidget(self.drop_input)
        self.verticalLayout_2.addWidget(self.drop_box)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.aggcurrent_box = QtWidgets.QGroupBox(self.tab_2)
        self.aggcurrent_box.setObjectName("aggcurrent_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.aggcurrent_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.aggcurrent_line = QtWidgets.QLineEdit(self.aggcurrent_box)
        self.aggcurrent_line.setInputMask("")
        self.aggcurrent_line.setAlignment(QtCore.Qt.AlignCenter)
        self.aggcurrent_line.setDragEnabled(False)
        self.aggcurrent_line.setReadOnly(True)
        self.aggcurrent_line.setClearButtonEnabled(False)
        self.aggcurrent_line.setObjectName("aggcurrent_line")
        self.verticalLayout_4.addWidget(self.aggcurrent_line)
        self.verticalLayout_3.addWidget(self.aggcurrent_box)
        self.agg_box = QtWidgets.QGroupBox(self.tab_2)
        self.agg_box.setObjectName("agg_box")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.agg_box)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.agg_min_btn = QtWidgets.QPushButton(self.agg_box)
        self.agg_min_btn.setObjectName("agg_min_btn")
        self.horizontalLayout_4.addWidget(self.agg_min_btn)
        self.agg_hour_btn = QtWidgets.QPushButton(self.agg_box)
        self.agg_hour_btn.setObjectName("agg_hour_btn")
        self.horizontalLayout_4.addWidget(self.agg_hour_btn)
        self.agg_day_btn = QtWidgets.QPushButton(self.agg_box)
        self.agg_day_btn.setObjectName("agg_day_btn")
        self.horizontalLayout_4.addWidget(self.agg_day_btn)
        self.agg_month_btn = QtWidgets.QPushButton(self.agg_box)
        self.agg_month_btn.setObjectName("agg_month_btn")
        self.horizontalLayout_4.addWidget(self.agg_month_btn)
        self.agg_hDay_btn = QtWidgets.QPushButton(self.agg_box)
        self.agg_hDay_btn.setObjectName("agg_hDay_btn")
        self.horizontalLayout_4.addWidget(self.agg_hDay_btn)
        self.verticalLayout_3.addWidget(self.agg_box)
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.cmd_box = QtWidgets.QGroupBox(self.tab_2)
        self.cmd_box.setObjectName("cmd_box")
        self.gridLayout = QtWidgets.QGridLayout(self.cmd_box)
        self.gridLayout.setObjectName("gridLayout")
        self.showdata_btn = QtWidgets.QPushButton(self.cmd_box)
        self.showdata_btn.setObjectName("showdata_btn")
        self.gridLayout.addWidget(self.showdata_btn, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.cmd_box)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.plot_btn = QtWidgets.QPushButton(self.cmd_box)
        self.plot_btn.setObjectName("plot_btn")
        self.gridLayout.addWidget(self.plot_btn, 0, 1, 1, 1)
        self.stat_btn = QtWidgets.QPushButton(self.cmd_box)
        self.stat_btn.setObjectName("stat_btn")
        self.gridLayout.addWidget(self.stat_btn, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.cmd_box)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.cmd_box)
        self.display_box = QtWidgets.QGroupBox(self.tab_2)
        self.display_box.setObjectName("display_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.display_box)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.display_window = QtWidgets.QPlainTextEdit(self.display_box)
        self.display_window.setReadOnly(True)
        self.display_window.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.display_window.setObjectName("display_window")
        self.horizontalLayout_5.addWidget(self.display_window)
        self.verticalLayout_3.addWidget(self.display_box)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.error_dropmenu)
        MainWindow.setTabOrder(self.error_dropmenu, self.loadfile_input)
        MainWindow.setTabOrder(self.loadfile_input, self.loadfile_btn)
        MainWindow.setTabOrder(self.loadfile_btn, self.drop_input)
        MainWindow.setTabOrder(self.drop_input, self.aggcurrent_line)
        MainWindow.setTabOrder(self.aggcurrent_line, self.agg_min_btn)
        MainWindow.setTabOrder(self.agg_min_btn, self.agg_hour_btn)
        MainWindow.setTabOrder(self.agg_hour_btn, self.agg_day_btn)
        MainWindow.setTabOrder(self.agg_day_btn, self.agg_month_btn)
        MainWindow.setTabOrder(self.agg_month_btn, self.agg_hDay_btn)
        MainWindow.setTabOrder(self.agg_hDay_btn, self.display_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Welcome to the Analysis of household electricity consumption program "))
        self.error_box.setTitle(_translate("MainWindow", "Errorhandling"))
        self.error_dropmenu.setToolTip(_translate("MainWindow", "Click to select errorhandling mode"))
        self.error_dropmenu.setStatusTip(_translate("MainWindow", "Click to select errorhandling mode"))
        self.error_dropmenu.setItemText(0, _translate("MainWindow", "Forward fill (replace corrupt measurement with latest valid measurement)"))
        self.error_dropmenu.setItemText(1, _translate("MainWindow", "Backward fill (replace corrupt measurement with next valid measurement)"))
        self.error_dropmenu.setItemText(2, _translate("MainWindow", "Drop (delete corrupted measurements)"))
        self.loadfile_box.setTitle(_translate("MainWindow", "Filename"))
        self.loadfile_input.setToolTip(_translate("MainWindow", "Please enter a filename"))
        self.loadfile_input.setStatusTip(_translate("MainWindow", "Please enter a filename in this box"))
        self.loadfile_input.setPlaceholderText(_translate("MainWindow", "Please enter the name of the datafile. Ex: 2008.csv"))
        self.loadfile_btn.setToolTip(_translate("MainWindow", "Click to load data"))
        self.loadfile_btn.setStatusTip(_translate("MainWindow", "Click to load data from filename"))
        self.loadfile_btn.setText(_translate("MainWindow", "Load data"))
        self.drop_box.setTitle(_translate("MainWindow", "Drag and Drop"))
        self.drop_input.setToolTip(_translate("MainWindow", "Drag a file into this box to load it"))
        self.drop_input.setStatusTip(_translate("MainWindow", "Drag a file into this box to load it"))
        self.drop_input.setDocumentTitle(_translate("MainWindow", "dasd"))
        self.drop_input.setPlaceholderText(_translate("MainWindow", "Please drag a datafile into this box"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Load data"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Select this tab to load data"))
        self.aggcurrent_box.setTitle(_translate("MainWindow", "Current Aggregation"))
        self.aggcurrent_line.setToolTip(_translate("MainWindow", "This is the current aggregation"))
        self.aggcurrent_line.setStatusTip(_translate("MainWindow", "This box shows how the data is currently aggregated"))
        self.aggcurrent_line.setText(_translate("MainWindow", "Minutely aggregation"))
        self.agg_box.setStatusTip(_translate("MainWindow", "Click to aggregate for daily consumption"))
        self.agg_box.setTitle(_translate("MainWindow", "Aggregate data"))
        self.agg_min_btn.setToolTip(_translate("MainWindow", "Click to aggregate"))
        self.agg_min_btn.setStatusTip(_translate("MainWindow", "Click to aggregate for minutely consumption"))
        self.agg_min_btn.setText(_translate("MainWindow", "Minute (no aggregation)"))
        self.agg_hour_btn.setToolTip(_translate("MainWindow", "Click to aggregate"))
        self.agg_hour_btn.setStatusTip(_translate("MainWindow", "Click to aggregate for hourly consumption"))
        self.agg_hour_btn.setText(_translate("MainWindow", "Hourly"))
        self.agg_day_btn.setToolTip(_translate("MainWindow", "Click to aggregate"))
        self.agg_day_btn.setText(_translate("MainWindow", "Daily"))
        self.agg_month_btn.setToolTip(_translate("MainWindow", "Click to aggregate"))
        self.agg_month_btn.setStatusTip(_translate("MainWindow", "Click to aggregate for monthly consumption"))
        self.agg_month_btn.setText(_translate("MainWindow", "Monthly"))
        self.agg_hDay_btn.setToolTip(_translate("MainWindow", "Click to aggregate"))
        self.agg_hDay_btn.setStatusTip(_translate("MainWindow", "Click to aggregate for the hourly average"))
        self.agg_hDay_btn.setText(_translate("MainWindow", "Hour-of-day (hourly average)"))
        self.cmd_box.setTitle(_translate("MainWindow", "Commands"))
        self.showdata_btn.setText(_translate("MainWindow", "Show data"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Each zone"))
        self.comboBox.setItemText(1, _translate("MainWindow", "All zones"))
        self.plot_btn.setToolTip(_translate("MainWindow", "Click to visualize data"))
        self.plot_btn.setStatusTip(_translate("MainWindow", "Click to visualize data in plots"))
        self.plot_btn.setText(_translate("MainWindow", "Visualize data"))
        self.stat_btn.setToolTip(_translate("MainWindow", "Click to display statistics"))
        self.stat_btn.setStatusTip(_translate("MainWindow", "Click to display statistics based on currently aggregated data"))
        self.stat_btn.setText(_translate("MainWindow", "Display statistics"))
        self.display_box.setTitle(_translate("MainWindow", "Display window"))
        self.display_window.setToolTip(_translate("MainWindow", "This window will display any messages given"))
        self.display_window.setStatusTip(_translate("MainWindow", "This window will display any messages given"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Analysis"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Select this tab to analyze data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

