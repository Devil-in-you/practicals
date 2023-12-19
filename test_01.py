# Example of nested for loops 
#triangel pattern using '*'
# number of rows for the pattern
num_rows = int(input("Enter no. of rows: "))

# Outer loop for rows
for i in range(num_rows):
    # Inner loop for printing stars in each row
    # print(i) #test line
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row
