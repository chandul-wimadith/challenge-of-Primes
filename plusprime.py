import sympy as sp

def primes():
    primes = [sp.prime(prime) for prime in range(1, 13)]
    place = [n for n in range(2, 12)]
    result = []
    for p in place: 
        sum_value = primes[p-1] + primes[p]
        result.append(sum_value)
    return result

primes_numbers = [sp.prime(prime) for prime in range(1, 13)]

sum_of_even_primes = primes()


def even_elements():
    n = [n for n in range(1,70)]
    even_numbers = [num for num in n if num % 2 == 0]  # Change condition to check for even numbers
    return even_numbers


## compare
'''print("------------------------------------------")

print('X  :', x)
print("------------------------------------------")

print(' EVENS :',even_elements())
print("------------------------------------------")
'''
even_numbers =even_elements()
#converter
def converter(first,second):
    # Convert to sets
    set_x = set(first)
    set_y = set(second)
    missing_numbers = set_y - set_x
    return list(missing_numbers)

missing_numbers = converter(sum_of_even_primes,even_numbers)
'''print('Missing from x for y :',converter(x,y))
print("------------------------------------------")

print(p_out)
'''