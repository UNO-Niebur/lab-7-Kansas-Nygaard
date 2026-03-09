#Kansas Nygaard
#Lab 7

#Euler Project #6 Sum Square Difference

def main():
    sumOfSquares = 0
    sumOfNumbers = 0

    for i in range(1, 101):
        sumOfSquares += i * i #finds sum of squares e.g (1^2 + 2^2 +...)
        sumOfNumbers += i #find sum of (1-100)
    
    sumSquared = sumOfNumbers * sumOfNumbers #squares the sum of (1-100)
    difference = sumSquared - sumOfSquares #finds the difference
    print(difference)

if __name__ == "__main__":
    main()
