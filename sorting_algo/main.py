"""
Sound Sorting Visualizer - Modular Version
Entry point for the application
"""

from app import SoundSortingApp


def print_welcome():
    """Print welcome message and instructions"""
    print("🎵 Sound Sorting - Algorithms as Music")
    print("=" * 50)
    print("\nEach algorithm creates a unique musical pattern!")
    print("\nControls:")
    print("  1 - Bubble Sort (lots of small swaps)")
    print("  2 - Selection Sort (finds minimums)")
    print("  3 - Insertion Sort (builds sorted portion)")
    print("  4 - Merge Sort (divide and conquer)")
    print("  5 - Quick Sort (partition-based)")
    print("  R - Reset/Shuffle")
    print("  Q - Quit")
    print("\nStarting visualizer...")
    print("=" * 50)


def main():
    """Main entry point"""
    print_welcome()
    
    app = SoundSortingApp(array_size=50)
    app.run()


if __name__ == "__main__":
    main()
