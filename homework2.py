# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    print(max(num1, num2, num3))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(*args):
    starting_value = 1
    for num in args:
        starting_value = (starting_value * num)
    return starting_value

# Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    concatenate = ''
    iterator = len(str)-1
    for i in str:
        concatenate = concatenate + str[iterator]
        iterator = iterator - 1
    return concatenate
    #return str[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1], [1,1]]
def pascal(n):
    if n < 1:
        print("Can't have 0 rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

max_num(2, 8, 5)
print(mult_list(2, 4, 8))
print(rev_string("pizza"))
print(num_within(3, 2, 4))
print(num_within(10, 2, 4))
print(pascal(8))


