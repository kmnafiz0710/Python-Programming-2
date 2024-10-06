# Check prime or Not prime.
def is_prime(Number):
    if Number <=1:
        return (f"{Number} is not a prime number")
    else:
        for n in range(2,int(Number**0.5)+1):
            if Number % n == 0:
                return (f"{Number} is not a prime number")
                break
        return f"{Number} is a prime number"

Number=int(input("Enter a number: "))
Prime_number=is_prime(Number)
print(Prime_number)