
from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, QTimer
from algorithms import ucs_steps, astar_steps
from node_item import NodeItem
from edge_item import EdgeItem
from graph import heuristic_lookup

class MapWidget(QWidget):
    stepCountChanged = pyqtSignal(int)
    stepReached = pyqtSignal(int, int, str)
    
    searchFinished = pyqtSignal(str, str, str, list, float)

    def __init__(self, graph, positions, heuristic_dict, parent=None):
        super().__init__(parent)
        self.graph = graph
        self.positions = positions
        self.heuristic = heuristic_dict
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHints(self.view.renderHints())
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

        self.node_items = {}
        self.edge_items = []
        self._build_scene()

        
        self.states = []
        self.current_index = -1
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._advance_autoplay)
        
        self.default_interval_ms = 600

        self.playing = False
        self.play_algorithm = None
        self.play_start = None
        self.play_goal = None

    def _build_scene(self):
        
        drawn = set()
        for u, nbrs in self.graph.items():
            if u not in self.positions:
                continue
            x1, y1 = self.positions[u]
            for v, cost in nbrs.items():
                if v not in self.positions:
                    continue
                key = tuple(sorted((u, v)))
                if key in drawn:
                    continue
                drawn.add(key)
                x2, y2 = self.positions[v]
                edge = EdgeItem(u, v, x1, y1, x2, y2, cost, parent=None)
                
                self.scene.addItem(edge)
                self.edge_items.append(edge)
        
        for name, (x, y) in self.positions.items():
            node = NodeItem(name, x, y)
            self.node_items[name] = node
            self.scene.addItem(node)

    
    def set_zoom(self, factor):
        
        self.view.resetTransform()
        self.view.scale(factor, factor)

    
    def run_search(self, algo_name, start, goal, autoplay=False, interval_ms=None):
        
        self.play_algorithm = algo_name
        self.play_start = start
        self.play_goal = goal

        self.reset()
        if algo_name == "UCS":
            gen = ucs_steps(start, goal, self.graph)
        else:
            gen = astar_steps(start, goal, self.graph, lambda n, g: heuristic_lookup(self.heuristic, n, g))

        
        self.states = list(gen)
        self.current_index = 0 if self.states else -1
        self.stepCountChanged.emit(len(self.states))

        if self.current_index >= 0:
            
            self.show_step(0)

        
        if autoplay and self.states:
            self.playing = True
            
            iv = interval_ms if interval_ms is not None else self.default_interval_ms
            self.timer.start(iv)

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.playing = False
        else:
            
            self.timer.start(self.default_interval_ms)
            self.playing = True

    def _advance_autoplay(self):
        
        if self.current_index < len(self.states) - 1:
            self.current_index += 1
            self.show_step(self.current_index)
        else:
            
            self.timer.stop()
            self.playing = False
            
            if self.states:
                node, _, _, path, cost = self.states[-1]
                
                self.searchFinished.emit(self.play_start, self.play_goal, self.play_algorithm, path, cost)

    def show_step(self, index):
        if not (0 <= index < len(self.states)):
            return
        self.current_index = index
        node, frontier, closed, path, cost = self.states[index]
        
        for n, ni in self.node_items.items():
            if n in closed:
                ni.set_closed()
            elif n in frontier:
                ni.set_frontier()
            elif n in path:
                ni.set_path()
            else:
                ni.set_default()
        if node in self.node_items:
            self.node_items[node].set_current()

        
        self._unhighlight_all_edges()
        self._highlight_path_edges(path)

        
        total = len(self.states)
        info_lines = []
        for i in range(index + 1):
            c, f, cl, p, ct = self.states[i]
            info_lines.append(f"Step {i+1}: Expanded {c} | Cost {ct} | Frontier {sorted(f)} | Closed {sorted(cl)} | Path {'->'.join(p)}")
        info_text = "\n".join(info_lines)
        self.stepReached.emit(index, total, info_text)

        
        if node == self.play_goal and (index == len(self.states) - 1):
            
            self.timer.stop()
            self.playing = False
            self.searchFinished.emit(self.play_start, self.play_goal, self.play_algorithm, path, cost)

    def next_step(self):
        if self.current_index < len(self.states) - 1:
            self.show_step(self.current_index + 1)

    def prev_step(self):
        if self.current_index > 0:
            self.show_step(self.current_index - 1)

    def reset(self):
        
        if self.timer.isActive():
            self.timer.stop()
        self.playing = False
        self.states = []
        self.current_index = -1
        for ni in self.node_items.values():
            ni.set_default()
        self._unhighlight_all_edges()
        self.stepCountChanged.emit(0)

    
    def _unhighlight_all_edges(self):
        for e in self.edge_items:
            e.unhighlight()

    def _highlight_path_edges(self, path):
        
        for a, b in zip(path, path[1:]):
            for e in self.edge_items:
                if {e.node_a, e.node_b} == {a, b}:
                    e.highlight()
                    break
