var1 = input("Enter the first value: ")
var2 = input("Enter the second value: ")
var3 = input("Enter the third value: ")
print(f"\nBefore swap: var1 = {var1}, var2 = {var2}, var3 = {var3}")
var1,var2,var3 = var3, var1, var2
print(f"After swap: var1 = {var1}, var2 = {var2}, var3 = {var3}")