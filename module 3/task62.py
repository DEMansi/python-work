#Write a Python program to returns sum of all divisors of a number 

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(int(input("Enter Value: "))))

#20=1+2+4+5+10
