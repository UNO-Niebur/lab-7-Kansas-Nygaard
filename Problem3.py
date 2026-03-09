#Kansas Nygaard
#Lab 7 Eulers Problems

#Problem #3 Largest Prime Factor

import NumberTests


#find largest prime factor of 600851475143
#test factors up to the square root of the number
def main():
    number = 600851475143
    largestPrimeFactor = 0
    i = 1
    
    while i * i <= number: #finds the square root of number
        if number % i == 0: #checks if i divides the number evenly
            if NumberTests.isPrime(i): #if i is prime save it
                largestPrimeFactor = i
                
            otherFactor = number // i #finds matching factor pair
            if NumberTests.isPrime(otherFactor): #checks if prime
                if otherFactor > largestPrimeFactor: #if prime and greater than previous factor replaces it
                    largestPrimeFactor = otherFactor
        i += 1
    print(largestPrimeFactor)


if __name__ == "__main__":
    main()