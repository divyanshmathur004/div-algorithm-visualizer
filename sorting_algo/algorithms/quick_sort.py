"""
Quick Sort implementation
"""

from sorting_algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    """Quick sort algorithm with visualization"""
    
    def get_name(self):
        return "Quick Sort"
    
    def sort(self):
        """Execute quick sort"""
        result = self._quick_sort_helper(0, len(self.array) - 1)
        if result:
            self.complete()
        return result
    
    def _quick_sort_helper(self, low, high):
        """Recursive quick sort helper"""
        if low < high:
            pi = self._partition(low, high)
            if pi is False:
                return False
            if not self._quick_sort_helper(low, pi - 1):
                return False
            if not self._quick_sort_helper(pi + 1, high):
                return False
        return True
    
    def _partition(self, low, high):
        """Partition the array around a pivot"""
        pivot = self.array[high]
        self.play_sound(pivot)
        i = low - 1
        
        for j in range(low, high):
            if self.check_quit():
                return False
            
            self.draw([j, high])
            self.play_sound(self.array[j])
            
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
            
            self.delay()
        
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1
