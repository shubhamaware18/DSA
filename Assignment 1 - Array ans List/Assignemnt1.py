# Q1 Given an array with some integer type values. Write a python script to sort array values.

def sort_array(arr):
    # sorting the list in reverse order and return it
    return sorted(arr,reverse=True)
arr = [1,2,5,4,97,3,515,98,63,2]
print(sort_array(arr))

#===============================================================#

# Q2. Given a list of Hetrogeneous elements. Write a python script to remove all the non int values from the list
## Solution-1
def remove_non_int_values(lst):
    # creating a empty list to store int element
    int_element = []
    # iterating over the list
    for item in lst:
        # if data type of current item is int the store it to empty list
        if type(item) == int:
            int_element.append(item)
        else:
            pass
    return int_element
lst = ["shubham", 45.5,"Pratik", 4, 8, 6546, (4,8,6,6), 44, 5.2]
print(remove_non_int_values(lst))

#===============================================================#

# Q3. Write a python code to calculate the avg of elements of a list

def get_avg_of_list(lst):
    return sum(lst) / len(lst)

arr = [1,2,5,4,97,3,515,98,63,2]
print(get_avg_of_list(arr))


#===============================================================#

# Q4. Write a python code to create a list of first N prime numbers

def create_list_of_prime(num):

    if num <= 1:
        return "Invalid Number"
    for i in range(2, num):
        if (num % i) == 0:
            return False
    
    return True

num = int(input('Enter a number: '))
lst = []
for i in range(1, num+1):
    if create_list_of_prime(i):
        lst.append(i)
    else:
        continue
print(lst)

#===============================================================#

# Q5. Write a python code to create a list of first N term of a Fibonacci series

def fibonacci(n):
    a, b = 0, 1
    if n <= a:
        return []
    elif n == b:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(b, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

n = 10
print(fibonacci(n))
