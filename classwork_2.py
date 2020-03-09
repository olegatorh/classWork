
num = int(input("Please enter the number of integers:"))
spisok = []
for i in range(0, num):
    spisok.append(int(input("Please enter the number: {}".format(i))))

print("Minimum is {}, Maximum is {}". format(min(spisok), max(spisok)))

massiv = []
factors3 = []
evens = []
notBy2nor3 = []

for i in range(1,11):
    massiv.append(i)

evens = [ k for k in massiv if k % 2 == 0]
factors3 = [ k  for k in massiv if k % 2 != 0 and k %3 == 0]
notBy2nor3 = [ k  for k in massiv if k % 2 != 0 and k % 3 != 0 ]
print(evens)
print(factors3)
print(notBy2nor3)

factorial = 1
number = int(input("Please enter the number:"))
for i in range(2,number + 1):
    factorial = factorial * i

print(factorial)


while ( input("Please enter the password:") != "First"):
    continue


while ( int(input("Please enter the number:")) > 0):
    continue

iterate = int(input("Please enter the number of integers:"))

for j in range(iterate):
    if int(input("Please enter the number:")) > 0 :
        continue
    else:
        break

