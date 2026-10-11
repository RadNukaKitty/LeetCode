class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        # index i (1-base) is special if it dvidies n evenly,
        # numbers only need to be checked up to sqrt(n)

        i = 1
        while i * i <= n:
            if n % i == 0:
                total += nums[i - 1] ** 2 # removes double counting squares

                j = n // i
                if j != i:
                    total += nums[j - 1] ** 2
            i += 1

        return total
        