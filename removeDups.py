class Solution:
    def removeDups(self):
        arr = [ 1, 1, 2, 3, 3, 3, 4, 5, 5, 6 ]
        left = 0
        right = 1

        while right < len(arr):
            if (arr[left] == arr[right]):
                arr.remove(right)
                # right += 1
            
            else:
                left = right
                right += 1

        return arr
    

solution = Solution()
print(solution.removeDups())