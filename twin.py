num=int(input(("enter the number  : ")))

def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(start, end):
   for i in range(start, end):
      if(i%2==1):
        j = i + 2
        if(is_prime(i) and is_prime(j)):
           print("{:d} and {:d}".format(i, j))

generate_twins(2, num)


# enter the number  : 20
# 3 and 5
# 5 and 7
# 11 and 13
# 17 and 19