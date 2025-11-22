<<<<<<< HEAD
#Python program to print bell number with row indices
#Bell Number:-Let S(n, k) be total number of partitions of n elements into k sets. The value of n'th Bell Number is sum of S(n, k) for k = 1 to n. Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)
#A sample Bell triangle is as follows:
#1
#1   3
#3   8   13
#13  23  33  43
#The code to print the bell triangle is as follows-
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
n = int(input("enter the number of bell: "))     #taking value from the user
bell = 0                                       #initialising bell to 'zero'
k = 0                                          #initialising k to 'zero'
for i in range(n):                         #loop for changing rows from 0 to n
    for j in range(i+1):                   #printing columns
        if j == 0 and i > 0:                     #repeating the last number of previous row in new row
            print(f"({i},{j}) {bell}", '', end='')            #printing first number of each line with row index
        else:
            k = (i**2)+1+bell                  #to generate other numbers of line
            print(f"({i},{j}) {k}", '', end='')               #printing other number in lines with row index
            bell = k                           #updating value of bell
    print('\n')                              #for moving into next lines
=======
# Standard Bell triangle (Bell numbers) generator and printer
# This implementation builds the Bell triangle using the well-known rule:
# - Row 0: [1]
# - Each row's first element is the last element of the previous row
# - Subsequent elements are produced by adding the previous element in the
#   current row to the element at the corresponding position in the previous row

def bell_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        # first element of row is last element of previous row
        row = [triangle[i-1][-1]]
        # fill remaining elements
        for j in range(1, i+1):
            row.append(row[-1] + triangle[i-1][j-1])
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    for row in triangle:
        print(' '.join(str(x) for x in row))

def main():
    try:
        n = int(input("enter the number of rows: "))
    except Exception:
        print("Invalid input: please enter a positive integer")
        return
    tri = bell_triangle(n)
    print_triangle(tri)
    # Print Bell numbers (last element of each row)
    if tri:
        print("Bell numbers:", [row[-1] for row in tri])

if __name__ == '__main__':
    main()
>>>>>>> 500b9e40c10188a50df617da6761bea63367f77c
