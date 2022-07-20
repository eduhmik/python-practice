class Solution:

    def twoSum(self, target, arr):

        visited = {}

        for i in range(len(arr)):
            complement = target - arr[i]
            if complement in visited:
                return [visited[complement], i]
            else:
                visited[arr[i]] = i
    
solution = Solution()
print(solution.twoSum(9, [2,7,11,15]))
