"""
Visualization renderer for the sorting algorithms
"""

import pygame
from constants import *


class Visualizer:
    """Handles all visual rendering"""
    
    def __init__(self, screen, array_size):
        """Initialize the visualizer"""
        self.screen = screen
        self.array_size = array_size
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def draw_array(self, array, highlights=None, sorted_indices=None, algorithm_name=""):
        """Draw the current state of the array"""
        self.screen.fill(BG_COLOR)
        
        if highlights is None:
            highlights = []
        if sorted_indices is None:
            sorted_indices = set()
        
        # Draw title
        title = self.font.render(f"Algorithm: {algorithm_name}", True, TEXT_COLOR)
        self.screen.blit(title, (20, 20))
        
        # Draw array as bars
        bar_width = (WINDOW_WIDTH - MARGIN) // self.array_size
        max_height = WINDOW_HEIGHT - BOTTOM_MARGIN - MARGIN
        
        for i, value in enumerate(array):
            bar_height = (value / self.array_size) * max_height
            x = 20 + i * bar_width
            y = WINDOW_HEIGHT - BOTTOM_MARGIN - bar_height
            
            # Choose color based on state
            if i in sorted_indices:
                color = SORTED_COLOR
            elif i in highlights:
                color = HIGHLIGHT_COLOR
            else:
                color = BAR_COLOR
            
            pygame.draw.rect(self.screen, color, 
                           (x, y, bar_width - BAR_SPACING, bar_height))
        
        # Draw instructions
        instructions = self.small_font.render(
            "Press: 1=Bubble | 2=Selection | 3=Insertion | 4=Merge | 5=Quick | R=Reset | Q=Quit",
            True, TEXT_COLOR
        )
        self.screen.blit(instructions, (20, WINDOW_HEIGHT - 30))
        
        pygame.display.flip()
