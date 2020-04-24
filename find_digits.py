
def findDigits(n):
    count = 0
    
    for i in list(str(n)):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count


test_case = int(input("enter number of test case:"))
for t_itr in range(test_case):
    n = int(input("enter the number:"))

result = findDigits(n)
print("count of number of digits in n that are divisors of n:",findDigits(n))
       
