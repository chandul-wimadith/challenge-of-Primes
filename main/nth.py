import math

def prime(n):
    total_sum = 0
    for i in range(1,pow(2,n)+1):
        inner_sum =0
        for j in range(1, i + 1):
           
            if j > 20:  
                break
            cos_value = math.cos(math.pi * (math.factorial(j - 1) + 1) / j)
            inner_sum += math.floor(pow(cos_value, 2))
            
        if inner_sum > 0:
            total_sum += math.floor(pow(n / inner_sum, 1 / n))
    
    return 1 + total_sum

hey = [prime(i) for i in range(1,60)]