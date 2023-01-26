class Solution:
    def addMultiplesOfFour(self):

        arr = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
        total = 0

        for i in range(len(arr)):
            if arr[i] % 4 == 0:
                total += arr[i]
        return total

solution = Solution()
print(solution.addMultiplesOfFour())