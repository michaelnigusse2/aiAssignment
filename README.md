# aiAssignment

1. Project Overview

Taxi Driver is a PyQt6-based graphical pathfinding visualizer that demonstrates two classical search algorithms:

Uniform Cost Search (UCS)
A* Search

The program loads a weighted graph representing parts of Addis Ababa from map.txt and displays it on an interactive map. Nodes and edges are rendered visually, and the user can observe each step of the search:

* Nodes explored
* Frontier expansion
* Final path highlighted
* Path cost
* Step-by-step navigation (Next / Previous)
* Reset and rerun options

This tool is designed for learning, experimentation, and demonstrating the differences between UCS and A*.


2. Project Structure

Your folder should look like this:

TaxiDriverAssignment/

│── main.py                 # Application entry point

│── mainwindow.py           # Main window logic

│── map_widget.py           # Handles graphics, scene, nodes, edges

│── node_item.py            # Node visualization (QGraphicsEllipseItem)

│── edge_item.py            # Edge visualization (QGraphicsLineItem)

│── graph.py                # Loads graph from map.txt and load heuristics from heuristic.txt

│── algorithms.py           # Contains both UCS and A* implementations

│── generate_heuristic.py   # Script to generate heuristic.txt automatically

│── map.txt                 # Integer-based weighted graph description

│── heuristic.txt           # Heuristic values for A*, format: "NodeA NodeB h"


3. Dependencies & Installation

Only one external dependency is required:

Install PyQt6:

bash
pip install PyQt6

Everything else uses only Python’s built-in standard library.


4. Running the Application
1


1. Navigate to the project directory:

bash
cd TaxiDriverAssignment

2. Run the main program:

bash
python main.py

or

bash
python3 main.py

The visualizer window will open, allowing you to:

* Select start and goal nodes
* Run UCS or A*
* Step through the algorithm
* View logs
* Reset and test another path


5. Data Files

1. map.txt

Contains integer costs for edges between locations, e.g.:

MeskelSquare Kazanchis 3
Bole Saris 4
Mexico Stadium 2

2. heuristic.txt

Contains heuristic values for A*, format:

MeskelSquare Kazanchis 1.8
Megenagna Bole 4.5

The A* implementation reads these values dynamically.


6. About the Algorithms

The file algorithmd.py contains both:

* A function for UCS
* A function for A*

Both algorithms share:

* A priority queue
* A cost dictionary
* A parent dictionary
* A closed list to avoid revisiting nodes

A* additionally incorporates heuristic values from heuristic.txt.


7. Credits

This project was created as part of an academic assignment on informed and uninformed search strategies, emphasizing visualization, cost-aware routing, and interaction.
