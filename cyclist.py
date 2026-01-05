spd1=int(input("What speed are you going at:"))
spd2=int(input("What speed are you going at:"))
spd3=int(input("What speed are you going at:"))
avg=(spd1+spd2+spd3)/3
print("Average speed of cyclist is",avg)
if avg>spd1:
    print("Cyclist 1 is the slowest")
if avg>spd2:
    print("Cyclist 2 is the slowest")
if avg>spd3:
    print("Cyclist 3 is the slowest")
else:
    print("They all are above average")
