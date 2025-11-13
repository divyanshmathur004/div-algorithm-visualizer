"""
Main application class for Sound Sorting Visualizer
"""

import pygame
import random
import time
from constants import *
from audio_engine import AudioEngine
from visualizer import Visualizer
from algorithms import (
    BubbleSort, 
    SelectionSort, 
    InsertionSort, 
    MergeSort, 
    QuickSort
)

class SoundSortingApp:
    """Main application class"""
    
    def __init__(self, array_size=DEFAULT_ARRAY_SIZE):
        """Initialize the application"""
        pygame.init()
        
        self.array_size = array_size
        self.array = list(range(1, array_size + 1))
        random.shuffle(self.array)
        
        # Initialize components
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sound Sorting - Algorithms as Music")
        
        self.audio = AudioEngine(array_size)
        self.visualizer = Visualizer(self.screen, array_size)
        
        # Algorithm registry
        self.algorithms = {
            pygame.K_1: BubbleSort,
            pygame.K_2: SelectionSort,
            pygame.K_3: InsertionSort,
            pygame.K_4: MergeSort,
            pygame.K_5: QuickSort,
        }
    
    def reset_array(self):
        """Shuffle the array"""
        self.array = list(range(1, self.array_size + 1))
        random.shuffle(self.array)
        self.visualizer.draw_array(self.array, algorithm_name="Ready - Choose an Algorithm!")
    
    def run_algorithm(self, AlgorithmClass):
        """Run a specific sorting algorithm"""
        self.reset_array()
        time.sleep(0.5)
        
        algorithm = AlgorithmClass(self.array, self.visualizer, self.audio)
        return algorithm.sort()
    
    def run(self):
        """Main event loop"""
        self.reset_array()
        running = True
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    
                    elif event.key == pygame.K_r:
                        self.reset_array()
                    
                    elif event.key in self.algorithms:
                        if not self.run_algorithm(self.algorithms[event.key]):
                            running = False
            
            pygame.display.update()
            clock.tick(60)  # 60 FPS
        
        pygame.quit()
