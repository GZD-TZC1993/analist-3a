power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

for i in range(2, 10, 3):
  print("The value of i is currently", i)

for i in range(1, 6):
    print("{}. mississippi".format(i))

print("Ready or not, here I come!")


# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


#tek sayı bulma

for i in range(1, 20):
 if i%2 == 1:
  print("tek sayı:",i)

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)
  

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#tersten yazdırma
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
