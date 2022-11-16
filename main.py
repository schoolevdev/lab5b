# Lab05bvst.py
# The "Sieve of Eratosthenes" Program
# This program names all primes from 1-n
# Evin Lodder 11/10
#
# Function <computePrimes> first creates a list of True elements.
# Nested loops alter the multiples of any prime number to False.
def computePrimes(n: int):  # -> list[bool] (3.10+ feature)
    print("COMPUTING PRIME NUMBERS\n")
    digitprimes = [0, 1, 2, 3, 5, 7]
    return_list = [] if n == 0 else [True] if n == 1 else [True, True]
    for i in range(3, n + 1):  # ignore evens
        # automatically append the digit primes
        if i in digitprimes:
            return_list.append(True)
            continue
        # check if it divides evenly by 3, 5, 7, or 9
        check: bool = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        return_list.append(check)
    return return_list


#
# Procedure <displayPrimes> visits every element in the <primes>
# list and displays the index values if the element is True (or prime).
# This procedures only displays 15 primes on one line.
def displayPrimes(primes) -> None:  # primes: list[bool]
    num = len(primes)
    print("PRIMES BETWEEN 1 AND ", num)
    count: int = 0
    for i in range(num):
        if count == 15:
            print()
            count = 0
        if primes[i]:
            print(i + 1, end=" ")
            count += 1


#######################################################
# Start of main execution loop
#
def main() -> None:
    max = eval(input("Enter primes upper-bound number: "))
    primes = computePrimes(max)
    displayPrimes(primes)
    #
    print("\nFINISHED")
    yn: str = input("Do you wish to repeat this program [Y/N]? ")
    if yn.lower() == "y":
        main()


if __name__ == "__main__":
    main()
