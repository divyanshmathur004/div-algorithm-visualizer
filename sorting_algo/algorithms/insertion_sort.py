"""
Insertion Sort implementation
"""

from sorting_algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    """Insertion sort algorithm with visualization"""
    
    def get_name(self):
        return "Insertion Sort"
    
    def sort(self):
        """Execute insertion sort"""
        self.sorted_indices = {0}
        
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            
            self.play_sound(key)
            
            while j >= 0 and self.array[j] > key:
                if self.check_quit():
                    return False
                
                self.draw([j, j + 1])
                
                self.play_sound(self.array[j])
                self.array[j + 1] = self.array[j]
                j -= 1
                self.delay()
            
            self.array[j + 1] = key
            self.sorted_indices.add(i)
            self.delay(0.025)
        
        self.complete()
        return True
