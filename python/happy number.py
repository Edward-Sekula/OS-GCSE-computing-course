def is_happy_number(n):
     seen = set()
     while True:
           digits = [int(c) for c in str(n)]
           n = sum(digit**2 for digit in digits)
           if n == 1:
                return True
           elif n in seen:
                return False
           seen.add(n)

 is_happy_number(1)
True
>>> is_happy_number(7)
True
>>> is_happy_number(11)
False
