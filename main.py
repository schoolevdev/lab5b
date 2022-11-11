# Lab05bvst.py
# The "Sieve of Eratosthenes" Program
# This program names all primes from 1-n
# Evin Lodder 11/10
#
# Function <computePrimes> first creates a list of True elements.
# Nested loops alter the multiples of any prime number to False.
def computePrimes(n: int):  # -> list[int] (3.10+ feature)
    print("COMPUTING PRIME NUMBERS\n")
    digitprimes = [0, 1, 2, 3, 5, 7]
    return_list = [] if n == 0 else [1] if n == 1 else [1, 2]
    for i in range(3, n + 1, 2):  # ignore evens
        # automatically append the digit primes
        if i in digitprimes:
            return_list.append(i)
            continue
        # check if it divides evenly by 3, 5, 7, or 9
        check: bool = True  # annoyingly, this is necessary since python doesn't have built-in double continue
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if not check:
            continue
        # if it doesn't divide evenly or is a digit prime, it's prime
        return_list.append(i)
    return return_list


#
# Procedure <displayPrimes> visits every element in the <primes>
# list and displays the index values if the element is True (or prime).
# This procedures only displays 15 primes on one line.
def displayPrimes(primes, num: int) -> None:  # primes: list[int]
    print("PRIMES BETWEEN 1 AND ", num)
    count: int = 0
    for i in primes:
        if count == 15:
            print()
            count = 0
        print(i, end=" ")
        count += 1


#######################################################
# Start of main execution loop
#
def main() -> None:
    max = eval(input("Enter primes upper-bound number: "))
    primes = computePrimes(max)
    displayPrimes(primes, max)
    #
    print("\nFINISHED")
    yn: str = input("Do you wish to repeat this program [Y/N]? ")
    if yn.lower() == "y":
        main()

if __name__ == "__main__":
    main()
