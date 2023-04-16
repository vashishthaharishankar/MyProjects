# write your code here
print("Select Options from Below:-\n1.At Most\n2.Exactly\n3.At Least\n4.Any Interval")
type = int(input())
n = int(input('Total no. of Samples: '))
if type == 4:
    lower = int(input('Lower Limit of Interval:'))
    upper = int(input('Upper Limit of Interval:'))
else:
    r = int(input('No. of Selected Samples: '))
success = float(input('Probability of Success: '))
failure = 1 - success


def fact_n(n):
    temp1 = n
    if n == 0 or n == 1:
        n_fact = 1
    else:
        for i in range(1, n):
            n_fact = temp1 * i
            temp1 = n_fact
    return n_fact


def fact_r(r):
    temp2 = r
    if r == 0 or r == 1:
        r_fact = 1
    else:
        for i in range(1, r):
            r_fact = temp2 * i
            temp2 = r_fact
    return r_fact


def fact_n_r(arg):
    temp3 = arg
    if arg == 0 or arg == 1:
        n_r_fact = 1
    else:
        for i in range(1, arg):
            n_r_fact = temp3 * i
            temp3 = n_r_fact
    return n_r_fact


final_probabilty = 0
if type == 1:
    type_name = 'At Most ' + str(r)
    for i in range(0, r + 1):
        a = fact_n(n)
        b = fact_r(i)
        c = fact_n_r(n - i)
        combination = a / (b * c)
        # Probability of Binomial Distribution
        # Probability = (nCr)*(P^r)*((P')^(n-r)) 
        prob = combination * (success ** i) * (failure ** (n - i))
        final_probabilty = prob + final_probabilty

elif type == 2:
    type_name = 'Exactly ' + str(r)
    for i in range(r, r + 1):
        a = fact_n(n)
        b = fact_r(i)
        c = fact_n_r(n - i)
        combination = a / (b * c)
        # Probability of Binomial Distribution
        # Probability = (nCr)*(P^r)*((P')^(n-r)) 
        prob = combination * (success ** i) * (failure ** (n - i))
        final_probabilty = prob + final_probabilty
elif type == 3:
    type_name = 'At Least ' + str(r)
    for i in range(r, n + 1):
        a = fact_n(n)
        b = fact_r(i)
        c = fact_n_r(n - i)
        combination = a / (b * c)
        # Probability of Binomial Distribution
        # Probability = (nCr)*(P^r)*((P')^(n-r)) 
        prob = combination * (success ** i) * (failure ** (n - i))
        final_probabilty = prob + final_probabilty
elif type == 4:
    type_name = '[' + str(lower) + ',' + str(upper) + ']'
    for i in range(lower, upper + 1):
        a = fact_n(n)
        b = fact_r(i)
        c = fact_n_r(n - i)
        combination = a / (b * c)
        # Probability of Binomial Distribution
        # Probability = (nCr)*(P^r)*((P')^(n-r)) 
        prob = combination * (success ** i) * (failure ** (n - i))
        final_probabilty = prob + final_probabilty
else:
    print('Invalid Selection!')

result = round(final_probabilty, 4)
print('Probabilty of Selecting', type_name, 'Samples out of', n, 'is:', result)