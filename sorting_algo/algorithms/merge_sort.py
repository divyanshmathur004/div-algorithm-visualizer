"""
Merge Sort implementation
"""

from sorting_algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    """Merge sort algorithm with visualization"""
    
    def get_name(self):
        return "Merge Sort"
    
    def sort(self):
        """Execute merge sort"""
        result = self._merge_sort_helper(0, len(self.array))
        if result:
            self.complete()
        return result
    
    def _merge_sort_helper(self, left, right):
        """Recursive merge sort helper"""
        if right - left <= 1:
            return True
        
        mid = (left + right) // 2
        if not self._merge_sort_helper(left, mid):
            return False
        if not self._merge_sort_helper(mid, right):
            return False
        return self._merge(left, mid, right)
    
    def _merge(self, left, mid, right):
        """Merge two sorted subarrays"""
        left_copy = self.array[left:mid].copy()
        right_copy = self.array[mid:right].copy()
        
        i = j = 0
        k = left
        
        while i < len(left_copy) and j < len(right_copy):
            if self.check_quit():
                return False
            
            self.draw([k])
            
            if left_copy[i] <= right_copy[j]:
                self.array[k] = left_copy[i]
                self.play_sound(left_copy[i])
                i += 1
            else:
                self.array[k] = right_copy[j]
                self.play_sound(right_copy[j])
                j += 1
            
            k += 1
            self.delay()
        
        while i < len(left_copy):
            if self.check_quit():
                return False
            self.array[k] = left_copy[i]
            self.play_sound(left_copy[i])
            i += 1
            k += 1
            self.delay()
        
        while j < len(right_copy):
            if self.check_quit():
                return False
            self.array[k] = right_copy[j]
            self.play_sound(right_copy[j])
            j += 1
            k += 1
            self.delay()
        
        return True
