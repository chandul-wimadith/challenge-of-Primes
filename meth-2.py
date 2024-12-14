from plusprime import even_numbers,sum_of_even_primes,primes_numbers,missing_numbers
 
from plusprime import converter
def method_2(even_numbers,sum_of_even_primes,primes_numbers,missing_numbers):
    primes_numbers = [n for n in primes_numbers if n % 2==1]

    new_list = [n for n in missing_numbers if any(n == 2 * x for x in primes_numbers)]
    
    return new_list

result = method_2(even_numbers,sum_of_even_primes,primes_numbers,missing_numbers)

sum_of_even_primes += result
sum_of_even_primes = sorted(sum_of_even_primes)
print(sum_of_even_primes)

#---------------------------

missing_numbers = converter(sum_of_even_primes,even_numbers)

print('missing numbers :',missing_numbers)
print(primes_numbers)
