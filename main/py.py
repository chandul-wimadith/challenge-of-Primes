from nth import prime

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pair_for_even_sum(target_even_sum):
    # Generate prime numbers up to the target even sum
    prime_numbers = [prime(n) for n in range(1, target_even_sum + 1) if prime(n) <= target_even_sum]

    # Find the largest prime number less than or equal to the target even sum
    for p in reversed(prime_numbers):
        complement = target_even_sum - p
        if is_prime(complement):
            return (p, complement)

    return None  # Return None if no pair is found

# Example usage
target_even_sum = 40
pair = find_prime_pair_for_even_sum(target_even_sum)

if pair:
    print(f"Pair of prime numbers that sum to {target_even_sum}: {pair}")
else:
    print(f"No prime pair found that sums to {target_even_sum}.")