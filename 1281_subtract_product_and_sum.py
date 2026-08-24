class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n 
        sum = 0 
        product = 1
        while temp>0:
            r= temp%10
            temp//=10
            sum +=r
            product *= r
        return product - sum 
