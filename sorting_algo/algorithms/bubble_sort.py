"""
Bubble Sort implementation
"""

from sorting_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    """Bubble sort algorithm with visualization"""
    
    def get_name(self):
        return "Bubble Sort"
    
    def sort(self):
        """Execute bubble sort"""
        n = len(self.array)
        
        for i in range(n):
            swapped = False
            
            for j in range(0, n - i - 1):
                if self.check_quit():
                    return False
                
                self.draw([j, j + 1])
                
                if self.array[j] > self.array[j + 1]:
                    # Play both values being swapped
                    self.play_sound(self.array[j])
                    self.delay(0.025)
                    self.play_sound(self.array[j + 1])
                    
                    # Swap
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
                    self.delay(0.025)
            
            self.sorted_indices.add(n - i - 1)
            
            if not swapped:
                # Add remaining elements to sorted
                for k in range(n - i):
                    self.sorted_indices.add(k)
                break
        
        self.complete()
        return True
