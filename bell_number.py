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
