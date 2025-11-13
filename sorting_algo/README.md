# Sound Sorting Visualizer - Modular Architecture

A modular, object-oriented implementation of sorting algorithm visualization with audio feedback.

## Project Structure

```
sorting/
├── constants.py              # Configuration and constants
├── audio_engine.py           # Audio generation and playback
├── visualizer.py             # Visual rendering
├── sorting_algorithm.py      # Abstract base class for algorithms
├── algorithms/               # Algorithm implementations
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
├── app.py                    # Main application class
├── main_modular.py           # Entry point (modular version)
└── main.py                   # Entry point (original monolithic version)
```

## Architecture

### 1. **Separation of Concerns**
- **constants.py**: All configuration values in one place
- **audio_engine.py**: Isolated audio generation logic
- **visualizer.py**: Pure rendering logic
- **sorting_algorithm.py**: Abstract interface for all algorithms

### 2. **Abstraction**
- `SortingAlgorithm` base class provides common functionality
- Each algorithm extends the base class and implements `sort()` method
- Consistent interface across all algorithms

### 3. **Modularity**
- Each algorithm in its own file
- Easy to add new algorithms by extending `SortingAlgorithm`
- Components can be tested independently

### 4. **Extensibility**
To add a new sorting algorithm:

```python
# algorithms/heap_sort.py
from sorting_algorithm import SortingAlgorithm

class HeapSort(SortingAlgorithm):
    def get_name(self):
        return "Heap Sort"
    
    def sort(self):
        # Implement your algorithm
        # Use self.draw(), self.play_sound(), etc.
        pass
```

Then register it in `app.py`:
```python
from algorithms import HeapSort

self.algorithms = {
    # ...existing algorithms...
    pygame.K_6: HeapSort,
}
```

## Usage

### Run the modular version:
```bash
python main_modular.py
```

### Run the original version:
```bash
python main.py
```

## Benefits of This Architecture

1. **Maintainability**: Each component has a single responsibility
2. **Testability**: Components can be unit tested independently
3. **Reusability**: AudioEngine and Visualizer can be reused in other projects
4. **Scalability**: Easy to add new algorithms without modifying existing code
5. **Readability**: Clear structure makes the code easier to understand

## Key Classes

- **AudioEngine**: Handles all sound generation
- **Visualizer**: Manages all visual rendering
- **SortingAlgorithm**: Abstract base for algorithm implementations
- **SoundSortingApp**: Main application controller

## Design Patterns Used

- **Strategy Pattern**: Interchangeable sorting algorithms
- **Template Method**: Base class defines structure, subclasses implement details
- **Facade Pattern**: SoundSortingApp provides simple interface to complex subsystems
