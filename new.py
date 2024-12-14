from plusprime import sum_of_even_primes,even_numbers
from plusprime import converter

# Define the missing and primes lists

missing = [32, 64, 66, 4, 40, 44, 16, 48, 50, 20, 54, 56, 28,64, 34, 58, 6, 38, 10, 14, 46, 22, 26, 62,64, 2, 4, 6, 58, 62]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227]

def find_sums_of_primes(missing, primes):
    # Create a new list to store elements from missing that can be formed by the sum of two distinct primes
    new_list = []

    # Check for sums of two distinct primes
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            prime_sum = primes[i] + primes[j]
            if prime_sum in missing:
                new_list.append(prime_sum)

    return new_list

# Call the function to find sums
result = find_sums_of_primes(missing, primes)

# Print the result

print(sorted(set(result)))

sum_of_even_primes += result
sum_of_even_primes.extend([2,4,6])
sum_of_even_primes = sorted(set(sum_of_even_primes))

print(sum_of_even_primes)

missing_numbers = converter(sum_of_even_primes,even_numbers)

print('missing numbers :',missing_numbers)