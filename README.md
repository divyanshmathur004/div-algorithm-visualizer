# Algorithm Visualizer

This repository contains an interactive **Algorithm Visualizer** built using Python and Pygame.  
It demonstrates how various **pathfinding algorithms** explore and solve a randomly generated maze in real time.

---

## Project Overview

### 📁 Key Files
- `main.py` — Entry point of the program  
- `maze.py` — Maze generation and cell structure  
- `algorithms.py` — Implementations of BFS, DFS, A* and Dijkstra  
- `visualizer.py` — Handles rendering, UI logic, solving, and statistics  
- `ui_components.py` — Buttons, dropdowns, labels, and UI styling  
- `constants.py` — Centralized colors, settings, and configuration  
- `pyproject.toml` — Project metadata and dependencies

---

## ✨ Features

### 🔹 Maze Generation
- Uses **recursive backtracking**  
- Produces a perfect maze with a unique solvable path

### 🔹 Pathfinding Algorithms
- **BFS (Breadth-First Search)**
- **DFS (Depth-First Search)**
- **A\* Search Algorithm**
- **Dijkstra’s Algorithm** 

Each algorithm is visualized step-by-step with different colors representing:
- Start / End nodes  
- Walls  
- Explored nodes  
- Visited nodes  
- Final shortest path  

### 🔹 Interactive Controls
- Click to place **Start** (green) and **End** (red)  
- Buttons to **Generate Maze**, **Solve**, **Reset**, **Clear Path**  
- Dropdown to select algorithms  
- Real-time **statistics panel** (time taken, nodes visited, path length)

---

## ▶️ How to Run

### 1. Create & activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # macOS/Linux
```
###2. Install dependencies
```bash
pip install pygame
```
3. Run the visualizer
```bash
python main.py
```
