"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

def findMedian():
    numbers.sort()
    medianPos = int(round((len(numbers)/2),1))
    if len(numbers) % 2 != 0:
        median = numbers[medianPos]
    else:
        num1 = numbers[medianPos-1]
        num2 = numbers[medianPos]
        median = (num1+num2)/2
    
    print(median)
    return(median)
()

def main():
    findMedian()

if __name__ == "__main__":
    main()


