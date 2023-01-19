class Solution:
    def divide(self, dividend, divisor):
        result = dividend/divisor
        return int(result)
    
a = Solution()
dividend = -2147483648
divisor = -1
print(a.divide(dividend,divisor))
