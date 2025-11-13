"""
Selection Sort implementation
"""

from sorting_algorithm import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    """Selection sort algorithm with visualization"""
    
    def get_name(self):
        return "Selection Sort"
    
    def sort(self):
        """Execute selection sort"""
        n = len(self.array)
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                if self.check_quit():
                    return False
                
                self.draw([min_idx, j])
                self.play_sound(self.array[j])
                self.delay()
                
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                # Play the swap
                self.play_sound(self.array[i])
                self.delay(0.025)
                self.play_sound(self.array[min_idx])
                
                self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
                self.delay(0.025)
            
            self.sorted_indices.add(i)
        
        self.complete()
        return True
