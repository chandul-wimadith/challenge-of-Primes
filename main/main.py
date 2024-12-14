from nth import prime
import matplotlib.pyplot as plt

n_term = 10

prime_numbers = [prime(n) for n in range(1,n_term+1)]
prime_plus_one = [num + 1 for num in prime_numbers]

sums = [prime_numbers[n] + prime_numbers[n+1] for n in range(n_term-1)]
even = [2 * n for n in range(1,n_term)]

x_values_primary = list(range(1,n_term+1))
x_value_sums = list(range(1,n_term))

plt.figure(figsize=(12, 8))

plt.plot(x_values_primary,prime_numbers,marker='o',label='Primary Numbers',color='blue')
plt.plot(x_values_primary,prime_plus_one,marker='s', label='Primary Numbers + 1', color='orange')
plt.plot(x_value_sums,sums,marker='^', label='Sum of Primary Numbers',color='green')
plt.plot(x_value_sums,even,marker='x',label='Even Numbers',color='red')

plt.title('bla bla bla ')
plt.xlabel('n (Position)')
plt.ylabel('Value')
plt.xticks(range(1, n_term + 1))
plt.legend()
plt.grid()

plt.show()