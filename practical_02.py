def swap_variables(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2

# Taking user input for two variables
variable1 = input("Enter the value for variable 1: ")
variable2 = input("Enter the value for variable 2: ")


# Swapping variables using the function
variable1, variable2 = swap_variables(variable1, variable2)

# Displaying values after being swapped
print("\nAfter swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)
