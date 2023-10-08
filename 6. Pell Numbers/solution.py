class Pell(object):
    def get(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        first, second = 0, 1
        while n > 1:
            first, second = second, first + 2 * second
            n -= 1
            print(first, second)
        return second
