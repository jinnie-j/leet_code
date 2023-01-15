class Solution:
    def search(self, A: List[int], target: int) -> int:
        n = len(A)
        left, right = 0, n - 1
        if n == 0: 
            return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target: 
                return mid
            
            if A[mid] >= A[left]:
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1