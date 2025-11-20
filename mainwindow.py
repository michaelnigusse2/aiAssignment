from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setWindowTitle("Taxi Driver - UCS / A* Visualizer")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        
        
        
        self.controlsLayout = QtWidgets.QHBoxLayout()
        self.controlsLayout.setObjectName("controlsLayout")

        
        self.labelStart = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelStart.setText("Start:")
        self.controlsLayout.addWidget(self.labelStart)

        
        self.startCombo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.controlsLayout.addWidget(self.startCombo)

        
        self.labelGoal = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelGoal.setText("Goal:")
        self.controlsLayout.addWidget(self.labelGoal)

        
        self.goalCombo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.controlsLayout.addWidget(self.goalCombo)

        
        self.runUcsBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.runUcsBtn.setText("Run UCS")
        self.controlsLayout.addWidget(self.runUcsBtn)

        
        self.runAstarBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.runAstarBtn.setText("Run A*")
        self.controlsLayout.addWidget(self.runAstarBtn)

        
        self.prevBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.prevBtn.setText("Previous")
        self.controlsLayout.addWidget(self.prevBtn)

        
        self.nextBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nextBtn.setText("Next")
        self.controlsLayout.addWidget(self.nextBtn)

        
        self.resetBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resetBtn.setText("Reset")
        self.controlsLayout.addWidget(self.resetBtn)

        
        self.speedSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.speedSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.controlsLayout.addWidget(self.speedSlider)

        self.verticalLayout.addLayout(self.controlsLayout)

        
        
        
        self.graphicsLayout = QtWidgets.QHBoxLayout()
        self.graphicsLayout.setObjectName("graphicsLayout")
        self.verticalLayout.addLayout(self.graphicsLayout)

        
        
        
        self.logText = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.logText.setObjectName("logText")
        self.verticalLayout.addWidget(self.logText)

        MainWindow.setCentralWidget(self.centralwidget)

        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
