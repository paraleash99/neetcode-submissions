class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)

        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1
    def get_next(self, n: int) -> int:
        total = 0
        while n>0:
            digit = n%10
            total += digit*digit
            n//=10
        return total