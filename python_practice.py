# function to determine maximum of three numbers
def max_num(x, y, z): 
    return max([x, y, z])

print (max_num(4, 8, 10))

# function to multiply all the numbers in a list
def mult_list(num):
    if len(num) ==0:
        return 0
    prod = num[0]

    if len(num) > 1:
        for i in num[1:]:
            prod = prod * i
    
    return prod

print(mult_list([1, 2, 3]))

# function to reverse a string
def rev_string(string):
    return string[::-1]

print(rev_string("hello"))

# function to check whether a number falls in a given range
def num_within(a,b,c):
    return a in range(b,c+1)

print(num_within(4,1,3))
print(num_within(4,1,10))


# function to print out the first n rows of Pascal's triangle
ptriangle = [[1],[1,1]]
def pascal(x):
    if x < 1:
        print('incorrect')
    elif x ==1:
        print(ptriangle[0])
    else:
        row_num = 2
        while len(ptriangle) < x:
            row = []
            row_prev = ptriangle[row_num - 1]

            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i >0 and i<length-1:
                    row.append(ptriangle[row_num-1][i-1]+ptriangle[row_num-1][i])
                else:
                    row.append(1)
                    ptriangle.append(row)
                    row_num += 1
                for row in ptriangle:
                    print(row)
pascal(4)




