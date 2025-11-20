import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from graph import load_graph, load_heuristic
from mainwindow import Ui_MainWindow
from map_widget import MapWidget

MAP_FILE = "map.txt"
HEUR_FILE = "heuristic.txt"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load graph & heuristic
        self.graph = load_graph(MAP_FILE)          # dict[node] -> {nbr: cost}
        self.heur = load_heuristic(HEUR_FILE)     # dict[(a,b)] -> cost

        # positions: keep your current pixel layout (you can replace with lat->xy results)
        positions = {
            "MeskelSquare": (211, 195),
            "Mexico": (121, 194),
            "SarBet": (89, 324),
            "Stadium": (186, 173),
            "Kazanchis": (290, 149),
            "BoleBrass": (391, 351),
            "BoleMedhanialem": (365, 311),
            "BoleAirport": (384, 355),
            "Olympia": (252, 240),
            "CMC": (697, 111),
            "Gotera": (184, 403),
            "Megenagna": (430, 122),
            "AratKilo": (224, 18),
            "Piassa": (173, 19),
            "Churchill": (162, 73),
            "Torhailoch": (0, 190),
            "OldAirport": (50, 386),
            "Saris": (269, 633),
            "Kaliti": (262, 1100),
            "Ayat": (800, 108),
            "Merkato": (60, 0),
            "AutobusTera": (61, 8),
        }

        # initialize map widget and put it in the UI placeholder
        self.map_widget = MapWidget(self.graph, positions, self.heur, parent=self)
        self.ui.graphicsLayout.addWidget(self.map_widget)

        # connect UI controls
        self.ui.startCombo.addItems(sorted(self.graph.keys()))
        self.ui.goalCombo.addItems(sorted(self.graph.keys()))

        # Run buttons become Play/Pause toggles
        self.ui.runUcsBtn.clicked.connect(self.on_run_ucs)
        self.ui.runAstarBtn.clicked.connect(self.on_run_astar)

        # Previous / Next / Reset unchanged
        self.ui.nextBtn.clicked.connect(self.map_widget.next_step)
        self.ui.prevBtn.clicked.connect(self.map_widget.prev_step)
        self.ui.resetBtn.clicked.connect(self.map_widget.reset)

        # repurpose slider for Zoom (0 .. 100 -> scale 0.5 .. 2.0)
        self.ui.speedSlider.setRange(1, 100)
        self.ui.speedSlider.setValue(50)  # default middle
        self.ui.speedSlider.valueChanged.connect(self.on_zoom_changed)
        # set initial zoom
        self.on_zoom_changed(self.ui.speedSlider.value())

        # hook widget signals for UI updates
        self.map_widget.stepCountChanged.connect(self.on_step_count_changed)
        self.map_widget.stepReached.connect(self.on_step_reached)
        self.map_widget.searchFinished.connect(self.on_search_finished)

    # Zoom slider handler
    def on_zoom_changed(self, value):
        # map slider (1..100) to scale factor 0.5 .. 2.0 (linear)
        min_scale, max_scale = 0.5, 2.0
        factor = min_scale + (value - 1) / 99.0 * (max_scale - min_scale)
        self.map_widget.set_zoom(factor)

    # Run/Pause toggles
    def on_run_ucs(self):
        btn = self.ui.runUcsBtn
        if btn.text() in ("Run UCS", "Run UCS ▶"):
            # start playing from start and change text to Pause
            start = self.ui.startCombo.currentText()
            goal = self.ui.goalCombo.currentText()
            if start == goal:
                QMessageBox.information(self, "Info", "Start and goal are the same.")
                return
            btn.setText("Pause ❚❚")
            # ensure A* button resets text if it was playing
            self.ui.runAstarBtn.setText("Run A*")
            self.map_widget.run_search("UCS", start, goal, autoplay=True)
        else:
            # currently running -> pause
            btn.setText("Run UCS ▶")
            self.map_widget.pause()

    def on_run_astar(self):
        btn = self.ui.runAstarBtn
        if btn.text() in ("Run A*", "Run A* ▶"):
            start = self.ui.startCombo.currentText()
            goal = self.ui.goalCombo.currentText()
            if start == goal:
                QMessageBox.information(self, "Info", "Start and goal are the same.")
                return
            btn.setText("Pause ❚❚")
            self.ui.runUcsBtn.setText("Run UCS")
            self.map_widget.run_search("A*", start, goal, autoplay=True)
        else:
            btn.setText("Run A* ▶")
            self.map_widget.pause()

    def on_step_count_changed(self, count):
        self.ui.statusbar.showMessage(f"Total steps: {count}")
        self.ui.prevBtn.setEnabled(True if count > 0 else False)
        self.ui.nextBtn.setEnabled(True if count > 1 else False)

    def on_step_reached(self, idx, total, info_text):
        # update log text area
        self.ui.logText.clear()
        self.ui.logText.append(info_text)
        self.ui.statusbar.showMessage(f"Step {idx+1}/{total}")

    def on_search_finished(self, start, goal, algorithm, path, cost):
        # Reset Run buttons text to original states
        self.ui.runAstarBtn.setText("Run A*")
        self.ui.runUcsBtn.setText("Run UCS")
        # Show final dialog
        path_str = " → ".join(path)
        msg = QMessageBox(self)
        msg.setWindowTitle("Search Finished")
        msg.setText(f"Start: {start}\nEnd: {goal}\nAlgorithm: {algorithm}\nPath: {path_str}\nCost: {cost}")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
