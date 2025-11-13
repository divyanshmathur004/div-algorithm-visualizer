"""
Abstract base class for sorting algorithms
"""

from abc import ABC, abstractmethod
import pygame
import time
from constants import NOTE_DURATION


class SortingAlgorithm(ABC):
    """Abstract base class for all sorting algorithms"""
    
    def __init__(self, array, visualizer, audio_engine):
        """Initialize the sorting algorithm"""
        self.array = array
        self.visualizer = visualizer
        self.audio = audio_engine
        self.sorted_indices = set()
        self.should_stop = False
    
    @abstractmethod
    def get_name(self):
        """Return the name of the algorithm"""
        pass
    
    @abstractmethod
    def sort(self):
        """Execute the sorting algorithm"""
        pass
    
    def check_quit(self):
        """Check if user wants to quit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                self.should_stop = True
                return True
        return False
    
    def draw(self, highlights=None):
        """Draw the current array state"""
        if highlights is None:
            highlights = []
        self.visualizer.draw_array(
            self.array, highlights, self.sorted_indices, self.get_name()
        )
    
    def play_sound(self, value):
        """Play a sound for the given value"""
        self.audio.play_value(value)
    
    def delay(self, duration=None):
        """Delay for visualization"""
        if duration is None:
            duration = NOTE_DURATION
        time.sleep(duration)
    
    def complete(self):
        """Mark sorting as complete"""
        self.sorted_indices = set(range(len(self.array)))
        self.draw()
        self.visualizer.draw_array(
            self.array, 
            sorted_indices=self.sorted_indices, 
            algorithm_name=f"{self.get_name()} - Complete!"
        )
