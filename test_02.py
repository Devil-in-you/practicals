
print("\nExample using break and continue in a loop")

# Using 'break' statement
print("Using 'break' statement:", end=" ")
i = 0
while i < 5:
    print(i, end=" ")
    if i == 2:
        break
    i += 1

# Using 'continue' statement
print("\n\nUsing 'continue' statement:", end=" ")
j = 0
while j < 5:
    j += 1
    if j == 2:
        continue
    print(j, end=" ")

print("\n\nProgram completed.\n")

